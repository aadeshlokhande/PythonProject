# constructor 
class Mobile:
    def __init__(self,price, model,ram,rom,brand):
        self.price = price
        self.model = model 
        self.ram = ram
        self.rom = rom 
        self.brand = brand

    def printData(self):
        print(f"price= {self.price}")
        print(f"model= {self.model}")
        print(f"ram= {self.ram}")
        print(f"rom= {self.rom}")
        print(f"brand= {self.brand}")


Honor8x = Mobile(15000,"Honor 8x", 4,64,"Honor")
Asuszetfone = Mobile(9000, "Asus zetfone max", 2,16,"Asus")

Asuszetfone.printData()

