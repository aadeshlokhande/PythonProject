# multilevel Inheritance

class A:
    def a(self):
        print("I am a A class")

class B(A):
    def b(self):
        print("I am a B class")

class C(B):
    def angry(self):
        print("I am a C class")

abc = C()
# ob1.a()
# ob1.b()
# ob1.c()
print(dir(abc)[27:])


