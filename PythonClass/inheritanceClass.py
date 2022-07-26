# single
# class Parents:
#     def parents(self):
#         print("I'm a Parent")

# class Child(Parents):
#     def child(self):
#         print("I'm child")

# obj = Child()
# obj.child()
# obj.parents()
# obj1 = Parents()
# obj1.parents()




# multiple
# class Mummy:
#     def mummy(self):
#         print("Mummy")

# class Daddy:
#     def daddy(self):
#         print("Daddy")

# class Child(Mummy,Daddy):
#     def child(self):
#         print("child")

# obj = Child()
# obj.child()
# obj.daddy()
# obj.mummy()





# hirachical
# class A:
#     def a(self):
#         print("A")

# class B(A):
#     def b(self):
#         print("B")
    
# class C(A):
#     def c(self):
#         print("C")  

# c = C()
# c.a()
# c.c()

# b = B()
# b.a()
# b.b()

# a = A()
# a.a()


# multilevel
# class A:
#     def a(self):
#         print("A")

# class B(A):
#     def b(self):
#         print("B")
    
# class C(B):
#     def c(self):
#         print("C")  

# c = C()
# c.a()
# c.b()
# c.c()

# b = B()
# b.a()
# b.b()

# a = A()
# a.a()
# ++++++++++++++++++++++++++++++

# class Value:
#     def getValue(self):
#         self.a = int(input("Enter = "))
#         self.b = int(input("Enter = "))

# class Greater(Value):
#     def checkGreater(self):
#         if(self.a>self.b):
#             print(f"{self.a} is greater")
#         else:
#             print(f"{self.b} is greater")
        
# class Op(Greater):
#     def add(self):
#         print(f"{self.a}+{self.b}={self.a+self.b}")  

# a = Op()
# a.getValue()
# a.checkGreater()
# a.add()