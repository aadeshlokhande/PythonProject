# if else ladder
# syntax:
# if(condition):
#     statements
# elif(condition):
#     statement
# elif(condition):
#     statement
# elif(condition):
#     statement
# elif(condition):
#     statement
# .
# .
# # .
# # else:
# # #     statement
# #
# # example;
# # num = int(input("Enter a number = "))
# # if(num==1):
# #     print("One")
# # elif(num==2):
# #     print("two")
# # elif(num==3):
# #     print("three")
# # else:
# #     print("invalid number")
#
# # one liner if else
# # print("YES") if (int(input("number = "))>18) else print("NO")
#
#
# #
# # def num2words(num):
# #
# #   ones =   ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
# #
# #   twos =   ['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
# #
# #  if(str[:19]):
# #      print("ones")
# #      if(str[20:90])
# #          print("twos")
#
#
# #
#
#
# # Main Logic
# ones = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')
#
# twos = ('Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')
#
# tens = ('Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred')
#
# suffixes = ('', 'Thousand', 'Million', 'Billion')
#
# def process(number, index):
#
#     if number=='0':
#         return 'Zero'
#
#     length = len(number)
#
#     if(length > 3):
#         return False
#
#     number = number.zfill(3)
#     words = ''
#
#     hdigit = int(number[0])
#     tdigit = int(number[1])
#     odigit = int(number[2])
#
#     words += '' if number[0] == '0' else ones[hdigit]
#     words += ' Hundred ' if not words == '' else ''

     # if(tdigit > 1):
#         words += tens[tdigit - 2]
#         words += ' '
#         words += ones[odigit]
#
#     elif(tdigit == 1):
#         words += twos[(int(tdigit + origin) % 10) - 1]
#
#     elif(tdigit == 0):
#         words += ones[odigit]
#
#     if(words.endswith('Zero')):
#         words = words[:-len('Zero')]
#     else:
#         words += ' '
#
#     if(not len(words) == 0):
#         words += suffixes[index]
#
#     return words;
#
# def getWords(number):
#     length = len(str(number))
#
#     if length>12:
#         return 'This program supports upto 12 digit numbers.'
#
#     count = length // 3 if length % 3 == 0 else length // 3 + 1
#     copy = count
#     words = []
#
#     for i in range(length - 1, -1, -3):
#         words.append(process(str(number)[0 if i - 2 < 0 else i - 2 : i + 1], copy - count))
#         count -= 1;
#
#     final_words = ''
#     for s in reversed(words):
#         temp = s + ' '
#         final_words += temp
#
#     return final_words
# #
# number = int(input('Enter any number: '))
# print('%d in words is: %s' %(number, getWords(number)))











