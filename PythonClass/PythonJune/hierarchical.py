# hierarchical inheritance

class Parent:
    def parent(self):
        print("I am parent")
    
class Son1(Parent):
    def son1(self):
        print("I am their first son")

class Son2(Parent):
    def son2(self):
        print("I am their second son")
    
arunTurkar = Parent()
arunTurkar.parent()

aryan = Son1()
aryan.son1()
aryan.parent()

arya = Son2()
arya.son2()
arya.parent()

print(dir(aryan)[26:])




# OOPs - Object-oriented programming

# class 
# object 
# inheritance
# polymorphism
# encapsulation
# abstraction