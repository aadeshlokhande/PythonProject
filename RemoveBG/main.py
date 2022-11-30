from rembg import remove
from PIL import Image

input = Image.open("man.jpg")
output = remove(input)
output.save("remove.png")



git status && git add . && git commit -m "msg" && git push origin -u main