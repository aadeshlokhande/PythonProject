# Hybrid Inheritance

class A:
    def a(self):
        print("A class")

class B(A):
    def b(self):
        print("B class")

class C(A):
    def c(self):
        print("C class")

class D(A):
    def d(self):
        print("D class")

class E(B,C):
    def e(self):
        print("E class")

class F(D):
    def f(self):
        print("F class")

class G(D,E):
    def g(self):
        print("G class")

class H(G):
    def h(self):
        print("H class")

class I(G):
    def i(self):
        print("I class")

class J(F,H):
    def j(self):
        print("J class")

OBA = A()
print(dir(OBA)[27:])

OBB = B()
print(dir(OBB)[27:])

OBC = C()
print(dir(OBC)[27:])

OBD = D()
print(dir(OBD)[27:])

OBE = E()
print(dir(OBE)[27:])

OBF = F()
print(dir(OBF)[27:])

OBG = G()
print(dir(OBG)[27:])

OBH = H()
print(dir(OBH)[27:])

OBI = I()
print(dir(OBI)[27:])

OBJ = J()
print(dir(OBJ)[27:])


