# class Car:
#     def car(self):
#         print("you can drive")
    
# class PetrolCar(Car):
#     def petrolCar(self):
#         print("you can fill petrol")
        
# class Ev(Car):
#     def ev(self):
#         print("you can charge your car")
        
# creta = PetrolCar()
# creta.car()
# creta.petrolCar()

# tesla = Ev()
# tesla.car()
# tesla.ev()
# --------------------------------


class TeaAndCoffie:
    def teaAndCoffie(self):
        print("you can order tea And Coffie")
    
class Cafe(TeaAndCoffie):
    def cafe(self):
        print("you can order nasta")
    
class Restro(TeaAndCoffie):
    def restro(self):
        print("you can order meal")
    
yellow_chilli = Cafe()
yellow_chilli.teaAndCoffie()
yellow_chilli.cafe()

madina = Restro()
madina.teaAndCoffie()
madina.restro()