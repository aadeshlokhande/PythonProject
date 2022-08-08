import os
folders = ["Bvoc","codeshot","CPP\ Projects","CProjects","Python\ Projects","WebsiteCalculator"]

for folder in folders:
    os.system(f"cd /home/coder/Documents/MyProjects/{folder}")
    os.system("git status && git add . && git commit -m \"none\" && git push -u origin main")