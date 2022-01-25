
#MODUŁ I, zadania rownież: FOLDER First Module

# 2. The math module couples more than 50 symbols 
# (functions and constants) that perform mathematical operations (like sine(), pow(), factorial()) or providing important values (like π and the Euler symbol e).
# 3. The random module groups more than 60 entities designed to help you use pseudo-random numbers. Don't forget the prefix "random", 
# as there is no such thing as a real random number when it comes to generating them using the computer's algorithms.
# 4. The platform module contains about 70 functions which let you dive into the underlaying layers of the OS and hardware. 
# Using them allows you to get to know more about the environment in which your code is executed.
from random import choice, sample
from math import pi as PI
import math

#GENEROWANIE
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(PI)
print(choice(my_list))
print(sample(my_list, 1))
print(sample(my_list, 10))


#OPERATING SYSTEM
#https://docs.python.org/3/py-modindex.html PYTHON MODULE INDEX
from platform import platform
platform(aliased = False, terse = False)
print(platform(0, 1))


from platform import machine
print(machine())

from platform import processor
print(processor())

from platform import system
print(system())

from platform import version
print(version())



from platform import python_implementation, python_version_tuple
print(python_implementation(), end=":  ")
for atr in python_version_tuple():
    print(atr, end=".")

    # python_implementation() → returns a string denoting the Python implementation (expect CPython here, unless you decide to use any non-canonical Python branch)

    # python_version_tuple() → returns a three-element tuple filled with:
    #     the major part of Python's version;
    #     the minor part;
    #     the patch level number.


import os
dir(os) #prints out the list of all the os module's facilities you can use in your code.

#EX1:
result = math.e == math.exp(1) #True

#EX2: Complete Sentence
#Setting the generator's seed with the same value each time your program is run guarantees that...
#... the pseudo-random values emitted from the random module will be exactly the same. 

import platform
print("")
print(len(platform.python_version_tuple()))


#MODULE.PY
import module


the_list = ['Where', 'are', 'the', 'snows?']
s = '*'.join(the_list)
print(s) #Where*are*the*snows?

s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s) #It is either hard or possible



#STRINGI MODULE 2
t = 'theta'
print(t.find('eta')) #1 index
print(t.find('et')) #-1 not found
print(t.find('the')) #2 index
print(t.find('ha')) #2 index

t = "zeta"; print(t.endswith("a"))
print('lambda30'.isalnum()) #isalnum() checks if the string contains only digits or alphabetical characters (letters), and returns True or False according to the result.
print(",".join(["omicron", "pi", "rho"])) #omicron,pi,rho
print("pythoninstitute.org".lstrip(".org"))
print("[" + " tau ".lstrip() + "]")
print("This is it!".replace("is", "are"))


print("[" + " upsilon ".rstrip() + "]") #[ upsilon]   () spacje wtedy tylko obcina 
print("cisco.com".rstrip(".com")) #cis

print("phi       chi\npsi".split()) #['phi', 'chi', 'psi']
# The split() method does what it says - it splits the string and builds a list of all detected substrings.

print("omega".startswith("meg")) #False
print("omega".startswith("om")) #True
# The startswith() method is a mirror reflection of endswith() - it checks if a given string starts with the specified substring.

print("[" + "   aleph   ".strip() + "]") #[aleph]
# The strip() method combines the effects caused by rstrip() and lstrip() - it makes a new string lacking all the leading and trailing whitespaces.

print("I know that I know nothing.".swapcase()) #i KNOW THAT i KNOW NOTHING.
print("I know that I know nothing. Part 1.".title()) #I Know That I Know Nothing. Part 1.
print("I know that I know nothing. Part 2.".upper()) #I KNOW THAT I KNOW NOTHING. PART 2.


# 1. Some of the methods offered by strings are:
# ord() and chr() functions  The chr() method returns a string representing a character whose Unicode code point is an integer.
#     capitalize() – changes all string letters to capitals;
#     center() – centers the string inside the field of a known length;
#     count() – counts the occurrences of a given character;
#     join() – joins all items of a tuple/list into one string;
#     lower() – converts all the string's letters into lower-case letters;
#     lstrip() – removes the white characters from the beginning of the string;
#     replace() – replaces a given substring with another;
#     rfind() – finds a substring starting from the end of the string;
#     rstrip() – removes the trailing white spaces from the end of the string;
#     split() – splits the string into a substring using a given delimiter;
#     strip() – removes the leading and trailing white spaces;
#     swapcase() – swaps the letters' cases (lower to upper and vice versa)
#     title() – makes the first letter in each word upper-case;
#     upper() – converts all the string's letter into upper-case letters.


# 2. String content can be determined using the following methods (all of them return Boolean values):

#     endswith() – does the string end with a given substring?
#     isalnum() – does the string consist only of letters and digits?
#     isalpha() – does the string consist only of letters?
#     islower() – does the string consists only of lower-case letters?
#     isspace() – does the string consists only of white spaces?
#     isupper() – does the string consists only of upper-case letters?
#     startswith() – does the string begin with a given substring?


    # a function named sorted(), creating a new, sorted list;
    # a method named sort(), which sorts the list in situ (itself)
