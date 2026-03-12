import os
import subprocess
import getpass
from datetime import datetime
import time

repo_path = r"E:\my project\private\robo fight"

os.chdir(repo_path)

username = getpass.getuser()

while True:

    status = subprocess.check_output("git status --porcelain", shell=True).decode()

    if status.strip() != "":

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"Auto update by {username} at {now}"

        subprocess.run("git add .", shell=True)
        subprocess.run(f'git commit -m "{message}"', shell=True)
        subprocess.run("git push", shell=True)

        print("Pushed:", message)

    else:
        print("No changes")

    time.sleep(3600)