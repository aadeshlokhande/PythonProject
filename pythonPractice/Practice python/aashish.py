num = int(input("How many numbers you have = "))
div = int(input("Enter a div = "))
sum = 0

for i in range(num):
    a = int(input("Enter a number = "))
    b = a/div 
    sum += b 
print(f"Total sum = {int(sum)}")