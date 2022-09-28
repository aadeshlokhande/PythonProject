# class and object(instance)

# class Student:
#     pass 

# sanket = Student()
# sanket.age = 20
# sanket.name = "sanket"
# sanket.address = "Nagpur"

# Ajay = Student()
# Ajay.age = 43
# Ajay.name = "Ajay"
# Ajay.address = "Pune"




class Student:
    def getData(self,age,name,address):
        self.Age = age 
        self.Name = name 
        self.Address = address
    
    def printData(self):
        print(f"Age = {self.Age}")
        print(f"Name = {self.Name}")
        print(f"Address = {self.Address}")
    

sanket = Student()
sanket.getData("20","Sanket","Nagpur")
# sanket.printData()
# print(sanket.Age)
print(dir(sanket))