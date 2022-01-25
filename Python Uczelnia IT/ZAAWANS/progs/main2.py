from sys import path

path.append('..\\packages\\extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB

print(sig.funS())
print(alp.funA())
print(funI())
print(funB())


#__module__ is a string, too - it stores the name of the module which contains the definition of the class.
class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)



#__bases__ is a tuple. The tuple contains classes (not class names) which are direct superclasses for the class.
class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)



    # introspection, which is the ability of a program to examine the type or properties of an object at runtime;
    # reflection, which goes a step further, and is the ability of a program to manipulate the values, properties and/or functions of an object at runtime.
#  If a class contains a constructor (a method named __init__) it cannot return any value and cannot be invoked directly.

#All classes (but not objects) contain a property named __name__, which stores the name of the class. Additionally, 
# a property named __module__ stores the name of the module in which the class has been declared, while the property named __bases__ 
# is a tuple containing a class's superclasses.
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy


sun = Star("Sun", "Milky Way")
print(sun)
# The default __str__() method returns the previous string - ugly and not very informative. You can change it just by defining your own method of the name.


# exceptions are classes
