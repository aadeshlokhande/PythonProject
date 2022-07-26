number = input("Enter a number = ")

unit = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",

 }

tens = {
    "1":"ten",
    "2":"twenty",
    "3":"thirty",
    "4":"fourty",
    "5":"fifty",
    "6":"sixty",
    "7":"seventy",
    "8":"eighty",
    "9":"ninty",
}

Hundred = {
    "1":"one hunderd",
    "2":"two hundred",
    "3":"three hundred",
    "4":"four hundred",
    "5":"five hundred",
    "6":"six hundred",
    "7":"seven hundred",
    "8":"eight hundred",
    "9":"nine hundred",
}

thousand = {
    "1" : "one thousands",
    "2" : "two thousands",
    "3" : "three thousands",
    "4" : "four thousands",
    "5" : "five thousands",
    "6" : "six thousands",
    "7" : "seven thousands",
    "8" : "eight thousands",
    "9" : "nine thousands"
}

a ={
    "11": 'eleven',
    "12": 'twelve',
    "13": 'thirteen',
    "14": 'fourteen',
    "15": 'fifteen',
    "16": 'sixteen',
    "17": 'seventeen',
    "18": 'eighteen',
    "19": 'nineteen',
}

if len(number)==1:
    if number=="0":
        print("Zero")
    else:
        print(unit[number])
elif len(number)==2:
    if number[0]=="1":
        print(a[number])
    else:
        print(tens[number[0]],unit[number[1]])

elif len(number) == 3:
    if number[1] == "1":
        print(Hundred[number[0]],a[number[1:]])
    elif number[2] == "0":
        print(Hundred[number[0]],tens[number[1]])
    else:
        print(Hundred[number[0]],tens[number[1]],unit[number[2]])

elif len(number)==4:
    if number[2] == "1":
        print(thousand[number[0]],Hundred[number[1]],a[number[2:]])
    elif number[3] == "0":
        print(thousand[number[0]],Hundred[number[1]],tens[number[2]])
    else:
        print(thousand[number[0]],Hundred[number[1]],tens[number[2]],unit[number[3]])

else:
    print("OUT OF RANGE")
