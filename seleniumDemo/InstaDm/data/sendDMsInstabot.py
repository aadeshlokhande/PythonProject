from instabot import Bot
import shutil
from time import sleep
# from fbid import ids,passwords
file = open("phillips.txt",'r')

msg = """hey, looking for Authentic Antiques & Collectibles?
'The Antique Hut' offers you one lakh square feet of display space featuring English, Chinese & French Furniture, Lalique, Wedgwood, Antique Porcelain, Glass, Vintage Lamps, Paintings, Victorian Bronze, French Chandeliers, Tapestries & Prints.
You name it we have it!
Visit our website: www.TheAntiqueHut.com

Follow: www.instagram.com/The_Antique_Hut

Like: www.facebook.com/TheAntiqueHut

Phone Number: +91 9175690000

DM or Call if you have any queries."""


for i in range(1):
    bot = Bot()
    list = []
    bot.login(username="code_karo", password = "CodeKaroInstagram<007>")
    
    for j in range(20):
        a = file.readline().replace("\n","")
        list.append(a)

    bot.send_message(msg,list)
    for u in list:
        print(u)
    sleep(5)


    shutil.rmtree("config")
file.close()