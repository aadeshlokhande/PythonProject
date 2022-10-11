# marksheet 
subject = ["hindi","marathi","English", "Geography","science","history"]
mark = [
    [76,58,64,67,78,58],
    [56,87,89,90,79,67],
    [45,77,78,75,46,98],
    [76,58,64,67,78,58],
    [56,87,49,90,79,67],
    [45,77,78,75,46,98],
    [76,58,64,67,78,58],
    [56,87,89,90,79,67],
    [45,77,78,75,46,98],
    [76,58,64,67,78,58],
    [56,87,89,90,79,67],
    [45,77,78,75,46,98],
    [76,58,64,67,78,58],
    [56,87,89,90,79,67],
    [45,77,78,75,46,98],
    [76,58,64,67,78,58],
    [56,87,89,90,79,67],
    [45,77,78,75,46,98],
    [76,58,64,67,78,58],
    [56,87,89,90,79,67],
]
print("press 1 : mark")
print("press 2 : result")
print("press 3 : Whole result")
choice = int(input("Enter your choice = "))

if(choice==1):
    rollnum = int(input("Enter a rollnumber = "))
    if(rollnum>=0 and rollnum<20):
        print("Press 0: hindi")
        print("Press 1: marathi")
        print("Press 2: english")
        print("Press 3: geography")
        print("Press 4: science")
        print("Press 5: history")
        sub = int(input("Enter a sub = "))
        print(f"roll number = {rollnum}\n{subject[sub]} = {mark[rollnum][sub]}")
    else:
        print("invalid roll number")

elif(choice==2):
    rollnum = int(input("Enter a rollnumber = "))
    for i in range(6):
        print(f"{subject[i]} = {mark[rollnum][i]}")

elif(choice==3):
    print("\t\thin\tmar\teng\tgeo\tsci\this\n")

    for i in range(20):
        print("roll no.",i,end="\t")
        for j in range(6):
            print(mark[i][j],end="\t")
        print()