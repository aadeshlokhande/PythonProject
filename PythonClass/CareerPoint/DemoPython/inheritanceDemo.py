# # Python program to demonstrate
# *******************single inheritance***********************
#
# # Base class
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
#
# # Derived class
# class Child(Parent):
#     def func2(self):
#         print("This function is in child class.")
#
# # Driver's code
# object = Child()
# object.func1()
# object.func2()

# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class
class Child(Parent):
    def func2(self):
        print("This function is in child class.")

# Driver's code
object = Child()
object.func1()
object.func2()


# # Python program to demonstrate
# **********************multiple inheritance************************
#
# # Base class1
# class Mother:
# 	mothername = ""
# 	def mother(self):
# 		print(self.mothername)
#
# # Base class2
# class Father:
# 	fathername = ""
# 	def father(self):
# 		print(self.fathername)
#
# # Derived class
# class Son(Mother, Father):
# 	def parents(self):
# 		print("Father :", self.fathername)
# 		print("Mother :", self.mothername)
#
# # Driver's code
# s1 = Son()
# s1.fathername = "RAM"
# s1.mothername = "SITA"
# s1.parents()




#Base class1
class Mother:
    mothername =""
    def mother(self):
        print(self.mothername)

#Base class2

class Father:
    fathername =""
    def father(self):
        print(self.fathername)

# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

# Driver's code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

