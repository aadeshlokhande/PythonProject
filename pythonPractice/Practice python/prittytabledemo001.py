# from prettytable import PrettyTable
# myTable = PrettyTable([1, 11, 21, 31, 41, 51, 61, 71, 81, 91])
# myTable.add_row([1+1, 1+11, 1+21, 1+31, 1+41, 1+51, 1+61, 1+71, 1+81, 1+91])
# myTable.add_row([2+1, 2+11, 2+21, 2+31, 2+41, 2+51, 2+61, 2+71, 2+81, 2+91])
# myTable.add_row([3+1, 3+11, 3+21, 3+31, 3+41, 3+51, 3+61, 3+71, 3+81, 3+91])
# myTable.add_row([4+1, 4+11, 4+21, 4+31, 4+41, 4+51, 4+61, 4+71, 4+81, 4+91])
# myTable.add_row([5+1, 5+11, 5+21, 5+31, 5+41, 5+51, 5+61, 5+71, 5+81, 5+91])
# myTable.add_row([6+1, 6+11, 6+21, 6+31, 6+41, 6+51, 6+61, 6+71, 6+81, 6+91])
# myTable.add_row([7+1, 7+11, 7+21, 7+31, 7+41, 7+51, 7+61, 7+71, 7+81, 7+91])
# myTable.add_row([8+1, 8+11, 8+21, 8+31, 8+41, 8+51, 8+61, 8+71, 8+81, 8+91])
# myTable.add_row([9+1, 9+11, 9+21, 9+31, 9+41, 9+51, 9+61, 9+71, 9+81, 9+91])

# print(myTable)


# from prettytable import PrettyTable
# myTable = PrettyTable([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# myTable.add_row([1*2, 2*2, 3*2, 4*2, 5*2, 6*2, 7*2, 8*2, 9*2, 10*2])
# myTable.add_row([1*3, 2*3, 3*3, 4*3, 5*3, 6*3, 7*3, 8*3, 9*3, 10*3])
# myTable.add_row([1*4, 2*4, 3*4, 4*4, 5*2, 6*4, 7*4, 8*4, 9*4, 10*4])
# myTable.add_row([1*5, 2*5, 3*5, 4*5, 5*5, 6*5, 7*5, 8*5, 9*5, 10*5])
# myTable.add_row([1*6, 2*6, 3*6, 4*6, 5*6, 6*6, 7*6, 8*6, 9*6, 10*6])
# myTable.add_row([1*7, 2*7, 3*7, 4*7, 5*7, 6*7, 7*7, 8*7, 9*7, 10*7])
# myTable.add_row([1*8, 2*8, 3*8, 4*8, 5*8, 6*8, 7*8, 8*8, 9*8, 10*8])
# myTable.add_row([1*9, 2*9, 3*9, 4*9, 5*9, 6*9, 7*9, 8*9, 9*9, 10*9])
# myTable.add_row([1*10, 2*10, 3*10, 4*10, 5*10, 6*10, 7*10, 8*10, 9*10, 10*10])

# print(myTable)


from prettytable import PrettyTable

myTable = PrettyTable(["Student Name", "Class", "Section", "Percentage"])

myTable.add_row(["saniya", "12th", "A", "91.08 %"])
myTable.add_row(["Rashmi", "12th", "C", "63.5 %"])
myTable.add_row(["sandip", "12th", "A", "90.23 %"])
myTable.add_row(["shubhangi", "12th", "D", "92.7 %"])
myTable.add_row(["achal", "12th", "A", "98.2 %"])
myTable.add_row(["Raj", "12th", "B", "88.1 %"])
myTable.add_row(["Ajay", "12th", "B", "95.0 %"])

print(myTable)