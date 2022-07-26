from googletrans import Translator, constants
from pprint import pprint


# init the Google API translator
translator = Translator()

path = "Data/words3000.txt"

file = open(path,'r')
words =file.read().split("\n")
file.close()

for word in words:

# word = "order"
    file = open("newtxt.txt",'a')
# # translate a spanish text to english text (by default)
    translation = translator.translate(word,dest='hi')
    # print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    trans = translation.text
    file.write(f"{word} : {trans}\n")
    file.close()
