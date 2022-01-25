print("I like to be a module.")


print(__name__) #Will print module in main.py

 

# This is how you can make use of the __main__ variable in order to detect the context in which your code has been activated:
# Updating the module.py file
print('---------------------------------------------if __name__ == "__main__":')
if __name__ == "__main__":
    print("I prefer to be a module.")
else:
    print("I like to be a module.")

# There's a cleverer way to utilize the variable, however. If you write a module filled with a number of complex functions, 
# you can use it to place a series of tests to check if the functions work properly.

# Each time you modify any of these functions, you can simply run the module to make sure that your amendments didn't spoil the code. 
# These tests will be omitted when the code is imported as a module.
 

""" module.py - an example of a Python module """

__counter = 0


def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)







#PATH
print("PATH")
import sys

print(sys.path[0]) #Current directory