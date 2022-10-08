# class Toy:
#     def __init__(self,a1,b1,c1):
#         self.a = a1 
#         self.b = b1 
#         self.c = c1 

#     def printKro(self):
#         print("a = ",self.a,self.b,self.c)

# shinchan = Toy(12,13,41)
# shinchan.printKro()








class Car:
    def __init__(self,milage1,average1,price1,name1):
        self.name = name1 
        self.milage = milage1
        self.average = average1
        self.price = price1
    def dederebaba(self):
        print("Name =",self.name)
        print("milage =",self.milage)
        print("price =", self.price)
        print("average =", self.average)

alto800 = Car(25,25,260000,f"Alto800")
nano = Car(30,30,150000,"Nano")

# alto800.dederebaba()
a =10
b = 20
print(a,"+",b,"=",a+b)