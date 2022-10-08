import requests

mainlink = ['num','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for ch in mainlink:
    url = f"https://www.computerhope.com/jargon/j{ch}.htm"

    html_content = str(requests.get(url).text)

    data= html_content.split("\n")

    list =[]
    for dataa in data:
        if("<a href=\"/jargon/" in dataa):
            list.append(dataa)

    list = list[3:-2]

    file = open("linka.txt","a")
    for i in list:
        url = i.split("\"")
        url = url[1]
        if("/jargon" in url):
            file.write(f"https://www.computerhope.com{url}\n")
    file.close()