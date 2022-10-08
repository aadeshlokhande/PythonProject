once={
    "0":"zero",
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

twoDigit ={
   "11":"eleven",
   "12":"twelve",
   "13":"thirteen",
   "14":"fourteen",
   "15":"fifteen",
   "16":"sixteen",
   "17":"seventeen",
   "18":"eighteen",
  "19":"nineteen"
}

tens={
    "1":"ten",
    "2":"twenty",
    "3":"thirty",
    "4":"fourty",
    "5":"fifty",
    "6":"sixty",
    "7":"seventy",
    "8":"eighty",
    "9":"nighty",
}

hundred={
    "1":"one hundred",
    "2":"two hundred",
    "3":"Three hundred",
    "4":"four hundred",
    "5":"five hundred",
    "6":"six hundred",
    "7":"seven hundred",
    "8":"eight hundred",
    "9":"nine hundred",
}

thousand={
    "1":"one thousand",
    "2":"two thousand",
    "3":"Three thousand",
    "4":"four thousand",
    "5":"five thousand",
    "6":"six thousand",
    "7":"seven thousand",
    "8":"eight thousand",
    "9":"nine thousand",
}

number = input("Enter the number :-> ")

if (len(number)==1):
    print(once[number])

elif (len(number)==2):          
    if(number[1]=="0"):           # 50
        print(tens[number[0]])
    elif(number[0]=="1"):         # 15
        print(twoDigit[number])
    else:
        print(tens[number[0]],once[number[1]])

elif (len(number)==3):
    if(number[1:]== "00"):
        print(hundred[number[0]])
    elif(number[2]=="0"):           
        print(hundred[number[0]],tens[number[1]])

    elif(number[0:2]=="00"):
        print(once[number[2]])

    elif(number[0]=="0"):
        if(number[2]=="0"):          
            print(tens[number[1]])
        elif(number[1]=="1"):         
            print(twoDigit[number])
        else:
            print(tens[number[1]],once[number[2]])
    
    elif(number[1]=="1"):        
        print(hundred[number[0]],twoDigit[number[1:]])
    elif(number[1]=="0"):
        print(hundred[number[0]],once[number[2]])
    else:
        print(hundred[number[0]],tens[number[1]],once[number[2]])

elif(len(number)==4):
    if(number[0]=="0"): #0004
        if(number[1]=="0"):
            if(number[2]=="0"):
                print(once[number])
            else:
                if(number[3]=="0"):           # 50
                    print(tens[number[2]])
                elif(number[2]=="1"):         # 15
                    print(twoDigit[number])
                else:
                    print(tens[number[2]],once[number[3]])
        else:
            if(number[2:]== "00"):
                print(hundred[number[1]])
            elif(number[3]=="0"):           
                print(hundred[number[1]],tens[number[2]])

            elif(number[1:3]=="00"):
                print(once[number[3]])

            elif(number[1]=="0"):
                if(number[3]=="0"):          
                    print(tens[number[2]])
                elif(number[2]=="1"):         
                    print(twoDigit[number])
                else:
                    print(tens[number[2]],once[number[3]])
            
            elif(number[2]=="1"):        
                print(hundred[number[1]],twoDigit[number[2:]])
            elif(number[2]=="0"):
                print(hundred[number[1]],once[number[3]])
            else:
                print(hundred[number[1]],tens[number[2]],once[number[3]])
    else:
        if(number[1:]== "000"):
            print(thousand[number[0]])
        elif(number[2:]== "00"):
            print(thousand[number[0]],hundred[number[2]])
        elif(number[2]=="0"):           
            print(thousand[number[0]],hundred[number[1]],once[number[2]])

        

        elif(number[1:3]=="00"):
            print(thousand[number[0]],once[number[3]])

        elif(number[1]=="0"): # 2050
            if(number[3]=="0"):          
                print(thousand[number[0]],tens[number[2]])
            elif(number[2]=="1"):         
                print(thousand[number[0]],twoDigit[number[2:]])
            else:
                print(thousand[number[0]],tens[number[2]],once[number[3]])
        elif(number[3]=="0"):           
            print(thousand[number[0]],hundred[number[1]],tens[number[2]])

        elif(number[2]=="1"):        
            print(thousand[number[0]],hundred[number[1]],twoDigit[number[2:]])
        elif(number[2]=="0"):
            print(thousand[number[0]],hundred[number[1]],once[number[2]])
        else:
            print(thousand[number[0]],hundred[number[1]],tens[number[2]],once[number[3]])

else:
    print("only 4 digit number allowed")