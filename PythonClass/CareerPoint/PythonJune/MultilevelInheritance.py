# multilevel inheritance

class Grandpa:
    def __init__(self):
        print("I am a grandpa class")

    def grandpa(self):
        print("Champak chacha")
    
class Father(Grandpa):
    def __init__(self):
        print("I am a Father class")

    def father(self):
        print("Jethalal")

class Son(Father):
    def __init__(self):
        print("I am a Son class")

    def son(self):
        print("Tappu")

# obA = Grandpa()
# obA.grandpa()

# obB = Father()
# obB.father()
# obB.grandpa()

obC = Son()
obC.son()
obC.father()
obC.grandpa()