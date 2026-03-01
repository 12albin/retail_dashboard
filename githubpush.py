import os
import subprocess
import shutil

repo_path = r"retail.pbix"
commit_message = "Added latest Power BI report"
# ====== GIT COMMANDS ======
subprocess.run(["git", "add", "."], cwd=repo_path)
subprocess.run(["git", "commit", "-m", commit_message], cwd=repo_path)
subprocess.run(["git", "push"], cwd=repo_path)

print("File uploaded successfully!")
