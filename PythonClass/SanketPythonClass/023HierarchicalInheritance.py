# Hierarchical Inheritance

# class A:
#     def a(self):
#         print("A class")
        
# class B(A):
#     def b(self):
#         print("B class")
        
# class C(A):
#     def c(self):
#         print("C class")
        
        
# obA = A()
# obA.a()


# obB = B()
# obB.a()
# obB.b()

# obC = C()
# obC.c()
# obC.a()



# -------------------------------------

class GetValue:
    def getvalue(self):
        self.a = int(input("enter a num = "))
        self.b = int(input("enter a num = ")) 

class Addtion(GetValue):
    def add(self):
        print(f"{self.a} + {self.b} = {self.a+self.b}")

class Substraction(GetValue):
    def sub(self):
        print(f"{self.a} - {self.b} = {self.a-self.b}")


obA = Addtion()
obA.getvalue()
obA.add()

obC = Substraction()
obC.getvalue()
obC.sub()