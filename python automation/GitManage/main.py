import os
from datetime import date

folders = ["Bvoc","codeshot","CPP\ Projects","CProjects","Python\ Projects","WebsiteCalculator"]

today = date.today()
Date = today.strftime("%d-%m-%Y")

for folder in folders:
    print(folder)
    os.system(f'cd /media/coder/Linux\ Media/MyProjects/{folder} && git status && git add . && git commit -m "{Date}" && git push -u origin main')
    os.system("cd")
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n\n")


# cd /media/coder/Linux\ Media/MyProjects/Python\ Projects/python\ automation/GitManage && python3 main.py && cd
