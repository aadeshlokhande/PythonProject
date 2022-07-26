import requests
from bs4 import BeautifulSoup

list = [
    "Animals",
    "Anime",
    "Brands",
    "Cars",
    "Cartoons",
    "Celebrities",
    "Devices",
    "Fortnite",
    "Games",
    "Geography",
    "Holidays",
    "Motor",
    "Movies",
    "Music",
    "Nature",
    "Other",
    "Pokémon",
    "Religion",
    "Resolutions",
    "Space",
    "Sports",
    "Superheroes",
    "TV Shows",
]

for cat in range(len(list)):
    urls = f'https://wallpapercave.com/categories/{list[cat]}'
    grab = requests.get(urls)
    soup = BeautifulSoup(grab.text, 'html.parser')
    
    # opening a file in write mode
    f = open("catagory.txt", "a")
    f.write(f"<<<<<<<<<< {list[cat].upper()} >>>>>>>>>>>\n")
    # traverse paragraphs from soup
    for link in soup.find_all("a"):
        data = link.get('href')
        if ("-wallpa" in data):
            f.write(data)
            f.write("\n")
    f.write("\n")
    f.close()