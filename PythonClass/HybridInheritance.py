class A:
    def a(self):
        print("A")

class B(A):
    def b():
        print("B")

class C(A):
    def c(self):
        print("C")

class D(A):
    def d(self):
        print("D")


class E(B):
    def e(self):
        print("E")

class F(B):
    def f(self):
        print("F")

class G(F,C):
    def g(self):
        print("G")

class H(G):
    def h(self):
        print("H")

class I(G):
    def i(self):
        print("I")


a = A()
a.a()

g = G()
g.a()

h = H()
h.g()
h.b()
