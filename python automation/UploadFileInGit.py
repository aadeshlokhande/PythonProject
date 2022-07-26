import pyautogui as pg
from time import sleep 
msg = "Python Projects"
ssh =  "git@github.com:aadeshlokhande/PythonProjects.git"

sleep(5)
cmd = ['git init',
'git config user.name "Aadesh"',
'git config user.email "aadeshlokhande11@gmail.com"',
'git config --list',
'git status',
'git add .',
f'git commit -m "{msg}"',
'git branch -M main',
f'git remote add origin {ssh}',
'git branch -M main',
'git push -u origin main']

for i in range(len(cmd)):
    pg.write(cmd[i],0.05)
    pg.press("enter")
    sleep(5)