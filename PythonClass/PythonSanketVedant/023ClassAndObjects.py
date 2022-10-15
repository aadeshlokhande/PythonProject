# # class 
# class Student:
#     pass

# # object
# sanket = Student()
# sanket.name = "Sanket"
# sanket.age = 22
# sanket.std = "2nd year"
# sanket.roll = 50324

# vedant = Student()
# vedant.name = "vedant"
# vedant.age = 20
# vedant.std = "3rd"
# vedant.roll = 96363

# print(sanket.age)



# ------------------------------------------

class Student:
    def getData(self,name,age,std,roll):
        self.Name = name 
        self.Age = age 
        self.Std = std 
        self.Roll = roll
        
    def printData(self):
        print(f"name = {self.Name}")
        print(f"Age = {self.Age}")
        print(f"Std = {self.Std}")
        print(f"Roll = {self.Roll}")
        



vedant = Student()
vedant.getData("Vedant", 20, "3rd", 8342)
# vedant.printData()

sanket = Student()
sanket.getData("sanket", 21, "2nd", 7654)

aadesh = Student()
aadesh.getData("aadesh", 98, "phd", 98576)


sanket.printData()
vedant.printData()
aadesh.printData()