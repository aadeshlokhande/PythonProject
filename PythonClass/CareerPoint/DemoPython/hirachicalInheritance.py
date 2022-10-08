# # Python program to demonstrate
# # Hierarchical inheritance
#
# # Base class
# class Parent:
# 	def func1(self):
# 		print("This function is in parent class.")
#
# # Derived class
# class Child1(Parent):
# 	def func2(self):
# 		print("This function is in child 1.")
#
# # Derivied class2
# class Child2(Parent):
# 	def func3(self):
# 		print("This function is in child 2.")
#
# # Driver's code
# object1 = Child1()
# object2 = Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()




# ****************example 2*******************
# Base class
class value:
	x = 0
	y = 0
	def getvalue(self,x,y):
		self.x = int(input("Enter a value of x = "))
		self.y = int(input("Enter a value of y = "))
		# self.x = x
		# self.y = y

# Derived class1
class multi(value):
	def gunakar(self):
		print("gunakar",self.x * self.y)

# Derivied class2
class add(value):
	def berij(self):
		print("berij = ",self.x + self.y)

# Driver's code
obj1 = multi()
obj2 = add()

# obj1.getvalue(12,45)
obj1.getvalue()
obj1.gunakar()

# obj2.getvalue(34,65)
obj2.getvalue()
obj2.berij()
