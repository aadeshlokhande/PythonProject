# Inheritance in python
# there are 4 types of inheritance in python
# 1) Single Inheritance
# 2) Multiple Inheritance
# 3) Multilevel Inheritance
# 4) Hierarchical Inheritance


# 1) Single Inheritance

                    # (A)
                    #  |
                    #  V 
                    # (B)


# class Daddy:
#     def daddy(self):
#         print("I'm a Daddy")

# class Child(Daddy):
#     def child(self):
#         print("I'm a child")

# # gangaram = Daddy()
# # gangaram.daddy()

# sonu = Child()

# sonu.child()
# sonu.daddy()


# class Vehicle:
#     def vehicle_info(self,speed,price):
#         print("Speed =", speed)
#         print("Price =", price)

# class EV(Vehicle):
#     def ev(self,charging_time,running_average):
#         print("charging_time = ",charging_time)
#         print("running_average = ",running_average)

# OlaS1 = EV()

# OlaS1.vehicle_info("105 kmph","100000 RS")
# OlaS1.ev("4hour","120km")


#==========================================================
#================= Multiple Inheritance ===================
#==========================================================

# A,b---> c

# class Mummy:
#     def mummy(self):
#         print("I'm a Mummy")

# class Daddy:
#     def daddy(self):
#         print("I'm a Daddy")

# class Child(Mummy,Daddy):
#     def child(self):
#         print("I'm a child")

# tappu = Child()
# tappu.child()
# tappu.daddy()
# tappu.mummy()


# # Parent class 1
# class Person:
#     def person_info(self, name, age):
#         print('Inside Person class')
#         print('Name:', name, 'Age:', age)

# # Parent class 2
# class Company:
#     def company_info(self, company_name, location):
#         print('Inside Company class')
#         print('Name:', company_name, 'location:', location)

# # Child class
# class Employee(Person, Company):
#     def Employee_info(self, salary, skill):
#         print('Inside Employee class')
#         print('Salary:', salary, 'Skill:', skill)

# # Create object of Employee
# emp = Employee()

# # access data
# emp.person_info('Jessica', 28)
# emp.company_info('Google', 'Atlanta')
# emp.Employee_info(12000, 'Machine Learning')




# class Manchurian:
#     def manchurian_samagri(self,item1, item2,item3):
#         print("this is manchurian class")
#         print("item 1 = ",item1)
#         print("item 2 = ",item2)
#         print("item 3 = ",item3)

# class Noodles:
#     def noodles(self,item1):
#         print("this is Noodles class")
#         print("item1 = ",item1)

# class Manchurian_noodles(Manchurian,Noodles):
#     def manchurian_noodles(self,item1, item2,item3):
#         print("this is manchurian_noodles class")
#         print("item 1 = ",item1)
#         print("item 2 = ",item2)
#         print("item 3 = ",item3)

# obj = Manchurian_noodles()

# obj.noodles("maida")
# obj.manchurian_samagri("vegies","corn flour","refined oil")
# obj.manchurian_noodles("souces","ajino moto","spices")



# ***************Multi level inheritnce******************

# class Grandpa:
#     def grandpa(self):
#         print("I'm a grandpa")

# class Pappa(Grandpa):
#     def pappa(self):
#         print("Im a pappa")

# class Child(Pappa):
#     def child(self):
#         print("I'm a child")

# golu = Child()
# golu.child()
# golu.pappa()
# golu.grandpa()

# jethalal = Pappa()
# jethalal.child()




# class Dudh:
#     def dudh(self):
#         print("Protein")

# class Dahi(Dudh):
#     def dahi(self):
#         print("tasty")

# class Kadi(Dahi):
#     def kadi(self):
#         print("Grm")

# obj = Kadi()
# obj.dudh()





# ===================================================================
# ==================== hirachical inheritance =======================
# ===================================================================

# class Parents:
#     def Pappa(self):
#         print("Pappa")

# class Child1(Parents):
#     def child_1(self):
#         print("child1")

# class Child2(Parents):
#     def child_2(self):
#         print("child2")

# class Child3(Parents):
#     def child_3(self):
#         print("child3")

# obj1 = Child1()
# obj1.child_1()
# obj1.Pappa()

# obj2 = Child2()
# obj2.child_2()
# obj2.Pappa()

# obj3 = Child3()
# obj3.child_3()
# obj3.Pappa()





# example 2
# class Getvalue:
#     def getvalue(self):
#         a = int(input("Enter a value of a = "))
#         b = int(input("Enter a value of b = "))
#         return a,b 

# class Add(Getvalue):
#     def add(self,a,b):
#         print(a+b)

# class Sub(Getvalue):
#     def sub(self,a,b):
#         print(a-b)

# obj1 = Add()
# x,y = obj1.getvalue()
# obj1.add(x,y)

# obj2 = Sub()
# p,o = obj2.getvalue()
# obj2.sub(p,o)





# ===================================================================
# ======================= hibrid inheritance ========================
# ===================================================================


# class A:
#     def a(self):
#         print("a")

# class B(A):
#     def B(self):
#         print("b")


# class C(A):
#     def c(self):
#         print("c")

# class D(A):
#     def d(self):
#         print("d")

# class E(C,D):
#     def e(self):
#         print("e")


# class F(E):
#     def f(self):
#         print("f")

# class G(B,C):
#     def g(self):
#         print("g")

# class H(F,D):
#     def h(self):
#         print("h")

# h = H()
# h.a()
# h.c()
# h.d()
# h.e()
# h.f()
# h.h()

