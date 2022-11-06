# hierarchical inheritance

class Dad:
    def daddy(self):
        print("takla")
    
class Son(Dad):
    def son(self):
        print("guitar")
    
class Daughter(Dad):
    def daughter(self):
        print("read")
    
# vijay = Dad()
# vijay.daddy()

# chintu = Son()
# chintu.son()
# chintu.daddy()

chinti = Daughter()
chinti.daughter()
chinti.daddy()