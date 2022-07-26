import requests
from bs4 import BeautifulSoup
# from dowloadImg import download

pop = open("catagory.txt",'r')
catagory = pop.readlines()

for i in catagory:
    if "<<<" in i:
        print("______________")
        store = open("imgLinks.txt",'a')
        store.write(f"\n{i.strip()}\n")
        store.close() 
    else:
        urls = f'https://wallpapercave.com{i}'.strip()
        print(urls)
        grab = requests.get(urls)
        soup = BeautifulSoup(grab.text, 'html.parser')
        # path = "/home/diamond/Pictures/images/"
        store = open("imgLinks.txt",'a')
        store.write(f"+++++++{i.strip()}+++++++\n")
        store.close() 
        for link in soup.find_all("a"):
            data = link.get('href')
            if("/download/" in data):
                link = f"https://wallpapercave.com{data}\n"
                store = open("imgLinks.txt",'a')
                store.write(link)
                store.close() 
                url = link.strip()
                print(link)
                # download(url,path)
pop.close()


print("DONE")