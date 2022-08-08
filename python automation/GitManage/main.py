import os
from datetime import date

folders = ["Bvoc","codeshot","CPP\ Projects","CProjects","Python\ Projects","WebsiteCalculator"]

today = date.today()
Date = today.strftime("%d-%m-%Y")

for folder in folders:
    print(folder)
    os.system(f"cd /home/coder/Documents/MyProjects/{folder}")
    os.system(f'git status && git add . && git commit -m "{Date}" && git push -u origin main')
    os.system("cd")
    print("#########################################################################\n\n")

# cd /home/coder/Documents/MyProjects/Python\ Projects/python\ automation/GitManage && python3 main.py