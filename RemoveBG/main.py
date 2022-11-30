from rembg import remove
from PIL import Image

input = Image.open("man.jpg")
output = remove(input)
output.save("remove.png")


