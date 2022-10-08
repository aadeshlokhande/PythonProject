students = {"doraemon":0, "nobita":1, "chinchan":2,"mickey mouse":3, "pikachu":4, "ninja hattodi":5, "suniyo":6, "chhota bheem":7, "jaggu":8, "chutki":9}
marks = {
    "mar"   : [12,45,84,69,21,45,96,21,45,63],
    "hin"   : [15,48,96,21,45,63,69,21,45,96],
    "eng"   : [15,62,46,69,14,23,48,96,21,45],
    "mat"   : [15,48,96,21,45,63,45,63,69,21],
    "his"   : [15,62,46,69,14,23,45,63,45,63],
    "geo"   : [12,45,84,69,21,45,46,69,14,23]
}
sub = ["mar","hin","eng","mat","his","geo"]

print("\t\t\t********MARKSHEET********\npress 1 : see marks\npress 2 : see student result\npress 3 : see whole result")
choice = int(input("Enter your choice = "))






if (choice==1):
    student = input("Enter student name = ")       # jaggu
    subject = input("Enter subject name = ")        # hindi

    print("\nRoll number =",students[student])
    print(student,"ko",subject, "me",marks[subject][students[student]],"Marks hai")

elif(choice==2):
    student = input("Enter student name = ")
    for i in sub:
        print(i,"\t=>\t",marks[i][students[student]])

elif(choice==3):
    print("\t\t************TOTAL MARKSHEET************")
    print("\t\t",end="")
    for i in sub:
        print(i,end="\t\t")
    cc = 0
    print()
    for roll in range(10):
        print(cc,end="")
        for mark in marks:
            print("\t\t",marks[mark][roll],end="")
        print()
        cc = cc + 1
