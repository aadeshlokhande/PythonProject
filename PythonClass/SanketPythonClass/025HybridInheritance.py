# Hybrid Inheritance

class A:
    def a(self):
        print("I am a A class")

class B(A):
    def b(self):
        print("I am a B class")

class C(A):
    def c(self):
        print("I am a C class")

class D(A):
    def d(self):
        print("I am a D class")

class E(B,D):
    def e(self):
        print("I am a E class")

class F(C):
    def f(self):
        print("I am a F class")

class G(D,F):
    def g(self):
        print("I am a G class")

class H(G):
    def h(self):
        print("I am a H class")

class I(G):
    def i(self):
        print("I am a I class")

class J(G):
    def j(self):
        print("I am a J class")

class K(H,I):
    def k(self):
        print("I am a K class")

print("--------obA---------")
obA = A()
print(dir(obA)[26:])

print("--------obB---------")
obB = B()
print(dir(obB)[26:])

print("--------obC---------")
obC = C()
print(dir(obC)[26:])

print("--------obD---------")
obD = D()
print(dir(obD)[26:])

print("--------obE---------")
obE = E()
print(dir(obE)[26:])

print("--------obF---------")
obF = F()
print(dir(obF)[26:])

print("--------obG---------")
obG = G()
print(dir(obG)[26:])

print("--------obH---------")
obH = H()
print(dir(obH)[26:])

print("--------obI---------")
obI = I()
print(dir(obI)[26:])

print("--------obJ---------")
obJ = J()
print(dir(obJ)[26:])

print("--------obK---------")
obK = K()
print(dir(obK)[26:])