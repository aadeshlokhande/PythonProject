# class class_name:
#     objects



# *************direct object creation***********
# class students:
#     pass
#
# himanshu = students()
# aadesh = students()
# gaurav = students()

# print(himanshu)
# print(aadesh)
# print(gaurav)

# himanshu.age = 17
# himanshu.std = "12th"
# himanshu.clg = "JVM"
#
# aadesh.age = 24
# aadesh.std = "1st year"
# aadesh.clg = "KNM"
#
# gaurav.age = 22
# gaurav.std = "BE"
# gaurav.clg = "Ycce"
#
# print(aadesh.age)
# print(himanshu.clg)



# *********** constructor and function ********
class student:
    def __init__(self,age,std,clg):
        self.age = age
        self.std = std
        self.clg = clg

    def getvalue(self):
        print("age = ",self.age)
        print("std = ",self.std)
        print("clg = ",self.clg)

himanshu = student(17,"12th","jvm")
aadesh = student(78,"bvoc","knm")
gaurav = student(190,"BE","ycce")
amisha = student(12,"43","ghf")

student.getvalue(amisha)
