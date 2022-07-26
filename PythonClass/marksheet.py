marks = [
    [12,36,45,64,35,23],
    [65,43,76,43,23,55],
    [67,55,34,62,64,88],
    [34,65,34,23,67,79],
    [54,23,56,76,35,23],
    [34,56,67,34,36,77],
    [54,23,56,76,35,23],
    [65,43,76,43,23,55],
    [34,65,34,23,67,79],
    [54,23,56,76,35,23]
]

sub = {
    "marathi" : 0,
    "hindi" : 1,
    "maths" : 2,
    "history" : 3,
    "geography" : 4,
    "science" : 5
}

print("press 1 : marks\npress 2 : result\npress 3 : whole result\n")
choice = int(input("enter your choice = "))
if(choice==1):
    roll_number = int(input("Enter a roll number = "))
    subject = input("Enter a subject = ")
    subject = subject.lower()
    if ((roll_number>=0) and (roll_number<10)):
        print("Marks = ",marks[roll_number][sub[subject]])
    else:
        print("we have 0 to 10 roll numbers")


elif(choice==2):
    roll_number  = int(input("Enter a roll number = "))
    if ((roll_number>=0) and (roll_number<10)):
        print("\nmarathi \t= ",marks[roll_number][0])
        print("hindi \t\t= ",marks[roll_number][1])
        print("maths \t\t= ",marks[roll_number][2])
        print("history \t= ",marks[roll_number][3])
        print("geography \t= ",marks[roll_number][4])
        print("science \t= ",marks[roll_number][5])
    else:
        print("we have 0 to 10 roll numbers")

elif(choice==3):
    print("\n*******************************RESULT*********************************")
    print("\t\tmar\thin\tmath\this\tgeo\tsci\n")
    for i in range(10):
        print("Roll no.",i,end="\t")
        for j in range(6):
            print(marks[i][j],end="\t")
        print("\n")
else:
    print("invalid option")