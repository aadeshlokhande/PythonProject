# # class - template
# class students:
#     pass
#
# chaitra = students()
# shivani = students()
# sahil = students()
#
# chaitra.fname = "Chaitra"
# chaitra.age = 14
# chaitra.standard = "9th"
#
# shivani.fname = "Shivani"
# shivani.age = 21
# shivani.standard = "MSC"
#
# sahil.fname = "Sahil"
# sahil.age = 17
# sahil.standard = "12th"
#
# print(chaitra.standard)
# print(shivani.fname)
# print(sahil.age)


class employee:
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def getvalues(self):
        print("my first name is",self.fname)
        print("my last name is",self.lname)
        print("my salary is",self.salary)

chaitra = employee("chitra","kharabe",15000)
chaitra.getvalues()

shivani = employee("shivani",'there',25000)
shivani.getvalues()

sahil = employee("sahil","nagrale",23000)
sahil.getvalues()