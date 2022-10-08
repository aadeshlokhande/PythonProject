class abc:
    a = 20
    b = "Hello"
    c = [12,543,65]

    def add(x,y):
        print(x+y)

abc.add(23,45)
print(abc.a)
print(abc.b)
print(abc.c[1])
abc.z = 12

print(abc.z)