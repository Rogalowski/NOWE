#MODULE.PY

from sys import path
path.append('//home//jacek//MegaSync//Python Uczelnia IT//ZAAWANS//First module//module')
import module
# from module import *
# from module import counter
# print("Counter: ", module.counter)

print("from module import suml, prodl:")
from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

#PATH
print("PATH")
import sys

for p in sys.path:
    print(p, end="------")
 



# we've doubled the \ inside folder name - do you know why?
# Because a backslash is used to escape other characters - if you want to get just a backslash, you have to escape it.

# we've used the relative name of the folder - this will work if you start the main.py file directly from its home folder, 
# and won't work if the current directory doesn't fit the relative path; you can always use an absolute path, like this:
# path.append('C:\\Users\\user\\py\\modules')
# we've used the append() method - in effect, the new path will occupy the last element in the path list; if you don't like the idea, you can use insert() instead.