import os
from datetime import date

folders = ["Bvoc","codeshot","CPP\ Projects","CProjects","Python\ Projects","WebsiteCalculator"]

today = date.today()
Date = today.strftime("%d-%m-%Y")

for folder in folders:
    os.system(f"cd /home/coder/Documents/MyProjects/{folder}")
    os.system(f'git status && git add . && git commit -m "{Date}" && git push -u origin main')

# cd /home/coder/Documents/MyProjects/Python\ Projects/python\ automation/GitManage