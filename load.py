import mysql.connector
import pandas as pd

connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234'
)

cursor=connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS demo")
print("database created")
cursor.execute('USE demo')

df=pd.read_excel('Online Retail.xlsx')
df = df.astype(object).where(pd.notnull(df), None)
table_name='onlineretail'
primary_key=''

def get_mysql_type(dtype):
    if 'int' in str(dtype):
        return 'INT'
    elif 'float' in str(dtype):
        return 'DOUBLE'
    elif 'datetime' in str(dtype):
        return 'DATETIME'
    else:
        return 'VARCHAR(255)'

column_sql=[]

for column in df.columns:
    mysql_type=get_mysql_type(df[column].dtype)
    column_sql.append(f"`{column}` {mysql_type}")

create_query=f" CREATE TABLE IF NOT EXISTS {table_name} ("

create_query+=",".join(column_sql)

if primary_key:
    create_query+=f", primary key('{primary_key}')"

create_query+=");"

print(create_query)
cursor.execute(create_query)

# cursor.execute('USE table onlineretail')

df=df.where(pd.notnull(df),None)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

column=",".join([f"`{col}`" for col in df.columns])
placeholder=", ".join(["%s"]*len(df.columns))

insert_query=f"INSERT INTO onlineretail ({column}) values({placeholder})"
data =[tuple(row) for row in df.to_numpy()]
cursor.executemany(insert_query,data)
connection.commit()
print("data inserted")


cursor.close()
connection.close()