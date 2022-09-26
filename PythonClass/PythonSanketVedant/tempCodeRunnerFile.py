def abc(a):
    if(a>=1):
        print("Hello",end=" ")
        abc(a-1)
    
abc(5)