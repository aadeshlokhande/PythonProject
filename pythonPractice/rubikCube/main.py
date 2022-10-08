from rubik_solver import utils

cube = {
    "y"     :   "yygyygywg",
    "b"     :   "oobbbbybw",
    "r"     :   "rgwrrrboo",
    "g"     :   "orywggbbg",
    "o"     :   "rggooowro",
    "w"     :   "rwwwwybyr"

}

centers ="ybrgow"

cubestr = ""
for center in centers:
    for i in cube[center]:
        cubestr = cubestr + i 


a= utils.solve(cube,"CFOP")

# counter = 0
# for color in centers:
#     for i in cubestr:
#         if i==color:
#             counter = counter + 1
#     print(color,counter)
#     counter = 0
    
    

