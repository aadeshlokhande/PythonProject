# polymorphism
# poly - many 
# morphism - forms 


# a = (12,43,62,32)
# # print(type(a))
# print(len(a))


# function overloading
# def calc(a,b,op):
#     if(op=="+"):
#         print(f"{a} + {b} = {a+b}")
#     if(op=='-'):
#         print(f"{a} - {b} = {a-b}")
#     if(op=="*"):
#         print(f"{a} x {b} = {a*b}")

# a = int(input("Enter a number = "))
# b = int(input("Enter a number = "))
# op = input("Enter a operator = ")

# calc(a,b,op)

# function overriding 
class parent:
    def info(self):
        print("Hello... I am a parent class")


class child:
    def info(self):
        print("Hello... I am a child class")

# jethalal = parent()
# jethalal.info()
# tappu = child()
# tappu.info()
# sanket = child()
# sanket.info()




a = parent()
b = child()


for i in [a,b]:
    i.info()



