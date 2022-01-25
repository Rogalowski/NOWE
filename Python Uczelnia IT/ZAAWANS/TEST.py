# import pygame

# run = True
# width = 400
# height = 100
# pygame.init()
# screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont(None, 48)
# text = font.render("Welcome to pygame", True, (255, 255, 255))
# screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# pygame.display.flip()
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT\
#         or event.type == pygame.MOUSEBUTTONUP\
#         or event.type == pygame.KEYUP:
#             run = False
 
 
# def mysplit(strng):
#     new_str = []
#     word = ""
#     for s in strng:
#         word == s
#         if s == " ":
#             new_str.append(word)
#             if new_str[-1]== "":
#                 del new_str[-1] 
#             word = ""
#         else:
#             word += s
 
#     new_str.append(word)       
#     if new_str[-1]== "":
#         del new_str[-1]     

#     return new_str


# print(mysplit("To be or not to be, that is the question"))
# print(mysplit("To be or not to be,that is the question"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))


# s1 = 'Where are the snows of yesteryear?'
# s2 = s1.split()
# s3 = sorted(s2)
# print(s3)



### ### ###   # ### ### ### ### ### # # 
# # # # # #   #   #   # #     # #   # # 
### # # ###   #   # ### ### ### ### ### 
  # # # # #   #   # #   # #   #   #   # 
### ### ###   #   # ### ### ### ###   # 

# list_8 = [
#     "###",
#     "# #",
#     "###",
#     "# #",
#     "###"
#     ]

 

# def numbers_str(char_num):
#     if char_num == 8:
#         return ("\n").join(list_8 )
#     if char_num == 0:
#         list_8[2] = "# #"
#         return ("\n").join(list_8 )
#     if char_num == 9:
#         list_8[-2] = "  #"
#         return ("\n").join(list_8 )
#     if char_num == 1:
#         list_8[0] = "  #"
#         list_8[1] = "  #"
#         list_8[2] = "  #"
#         list_8[3] = "  #"
#         list_8[4] = "  #"
#         return ("\n").join(list_8 )

# print(numbers_str(1))

# Caesar cipher.
# def Caesar():
#     text = input('Enter your message: ')
#     input_code = int(input('Enter your input_code: '))
#     if input_code > 90:
#         input_code -= 90
#     cipher = ''
#     for char in text:
#         if not char.isalpha():
#             continue
#         char = char.upper()
#         code = ord(char) + input_code
#         if code > ord('Z'):
#             code = ord('A')
#         cipher += chr(code)
#     return cipher, input_code

# print(Caesar())
 
# The code shows an extravagant way
# of leaving the loop.


 

# dictionary = { 'a': 'b', 'b': 'c', 'c': 'd' }
# ch = 'a'

# try:
#     while True:
#         ch = dictionary[ch]
#         print(ch)
# except KeyError:
#     print('No such key:', ch)
 
 
for x in open("file", "rt"):
  
  print(x)
  
  
x = bytearray(3)
print(x)

from datetime import datetime, date

datetime = datetime(2019, 11, 27, 11, 27, 22)
print(datetime.strftime("%y/%B/%d %H:%M:%S"))
print(datetime)
      
dat1 = date(1992,1 ,16)
dat2 = date(1991,1 ,16)
print(dat1- dat2)

numbers = [ 2 , 4, 7]
foo = map(lambda num: num ** 2, numbers)
print(foo)
var = 1
assert var !=0
print("\\\\")

print(__name__)
import os
print(os.uname())

for x in open('file', 'rt'):
  print(3)

import random
a = random.randint(0,100)
b = random.choice((0,100,3))
c = random.randrange(10,14,3)

print(a,b,c)