from bs4 import BeautifulSoup
import requests

file = open("glinks.txt", 'r')
urls = file.read().split("\n")
file.close()

for url in urls:
    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "html5lib")
    data = soup.prettify()
    data = data.split("\n")

    list = []
    for i in range(len(data)):
        if('<a href="/url?q=' in data[i]):
            link = data[i].strip()[16:].split("&amp")[0]
            list.append(link)

    file = open("links.txt",'a') 
    for i in range(10):
        print(list[i])
        file.write(f"{list[i]}\n")
    file.close()       