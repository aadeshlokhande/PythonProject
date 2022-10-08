file = open("Dataset_Updated1.csv",'r')
data = file.read()
file.close()

file = open("Dataset_Updated.csv",'w')

lines = data.split("\n")
file.write("Super built-up Area,availability,location,size_ BHK,society,total_sqft,bath,balcony,price\n")
for ln in range(13320):
    line = lines[ln].split(",")
    if(0<ln):
        for i in range(9):
            if(i==0):           # Super built-up Area
                if(line[i]!=""):
                    file.write(f"{line[i]},")
                else:
                    file.write(f"{line[i]},")
 

            if(i==1):           # availability
                if(line[i]!=""):
                    file.write(f"Ready to move,")    
                else:
                    file.write(f"{line[i]},")

            if(i==2):           # location
                if(line[i]!=""):
                    file.write(f"{line[i]},")    
                else:
                    file.write(f"{line[i]},")

            if(i==3):           # size_ BHK
                if(line[i]!=""):
                    file.write(f"{line[i]},")
                else:
                    file.write(f"{line[i]},")

            if(i==4):           # society
                if(line[i]!=""):
                    file.write(f"{line[i]},")
                else:
                    file.write(f"{line[i]},")

            if(i==5):           # total_sqft
                if(line[i]!=""):
                    file.write(f"{line[i]},")
                else:
                    file.write(f"{line[i]},")

            if(i==6):           # bath
                if(line[i]!=""):
                    file.write(f"{line[i]},")
                else:
                    file.write(f"{line[i]},")

            if(i==7):           # balcony
                if(line[i]==""):
                    file.write(f"1,")
                else:
                    file.write(f"{line[i]},")

            if(i==8):           # price
                if(line[i]!=""):
                    file.write(f"{int(float(line[-1]))}\n")

                    

    # except:
    #     file.write(f"price\n")
file.close()