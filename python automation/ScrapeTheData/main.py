import requests
from bs4 import BeautifulSoup
from dowloadImg import download
 
urls = 'https://wallpapercave.com/gnu-linux-wallpapers'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')
path = "/home/diamond/Pictures/images/"


for link in soup.find_all("a"):
    data = link.get('href')
    if("/download/" in data):
        link = f"https://wallpapercave.com/{data}\n"
        store = open("imgLinks.txt",'a')
        store.write(link)
        store.close() 
        url = link.strip()
        # download(url,path)


