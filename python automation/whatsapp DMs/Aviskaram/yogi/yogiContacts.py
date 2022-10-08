file = open("yogiContacts.txt",'r')
filew = open("contacts.txt",'w')


for i in range(3104):
    a = file.readline()
    filew.write(f"contact_{i},+91{a}")
