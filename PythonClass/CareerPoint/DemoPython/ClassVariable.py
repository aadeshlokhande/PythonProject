# class employee:
#     increament = 1.5
#     incr_year = 2
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def inyear(self):
#         self.incr_year = self.incr_year + 1
#
#     def inc(self):
#         self.salary = self.salary * employee.increament
#
#     def printData(self):
#         print("name = ",self.name)
#         print("Age = ", self.age)
#         print("Salary = ", int(self.salary))
#         print("Experiance = ",self.incr_year)
#
# chaitra = employee("chaitra",14,15000)
# shivani = employee("shivani",21,22000)
# sahil = employee("sahil",17,20000)
#
# sahil.printData()
# sahil.inc()
# sahil.inyear()
# sahil.printData()

class employee:
    increament = 1.5
    incr_year = 2
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def inyear(self):
        self.incr_year = self.incr_year + 1

    def inc(self):
        self.salary = self.salary * employee.increament

    def printData(self):
        print("name = ",self.name)
        print("Age = ", self.age)
        print("Salary = ", int(self.salary))
        print("Experiance = ",self.incr_year)

chaitra = employee("chaitra",14,15000)
shivani = employee("shivani",21,22000)
sahil = employee("sahil",17,20000)

sahil.printData()
sahil.inc()
sahil.inyear()
sahil.printData()

chaitra.printData()
chaitra.inc()
chaitra.inyear()
chaitra.printData()

shivani.printData()
shivani.inc()
shivani.inyear()
shivani.printData()