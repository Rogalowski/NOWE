
    # Generators, iterators and closures;
    # Working with file-system, directory tree and files;
    # Selected Python Standard Library modules (os, datetime, time, and calendar.)


def fun(n):
    for i in range(n):
        yield i


for v in fun(5):
    print(v)

for v in fun(5):
    print(v)



# What if you need a generator to produce the first n powers of 2?

# Nothing easier. Just look at the code below:

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)


# Can you guess the output? Copy the code to the editor and run it to check your guesses.

# List comprehensions

# Generators may also be used within list comprehensions, just like here:
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = [x for x in powers_of_2(5)]
print(t)
# The value it provides is equal to expression_one when the condition is True, and expression_two otherwise.

# A good example will tell you more. Look at the code in the editor.

# The code fills a list with 1's and 0s - if the index of a particular element is odd, the element is set to 0, and to 1 otherwise.

# Simple? Maybe not at first glance. Elegant? Indisputably.

# Can you use the same trick within a list comprehension? Yes, you can.
the_range = []
the_list = []

for x in range(10):
    the_range.append(x)
    the_list.append(1 if x % 2 == 0 else 0)

print(the_range)
print(the_list)
#LUB
the_list = []
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print(the_list)




#LAMBDA
#DLA CHĘTNYCH: Napisz w dwóch wersjach: def i lambda potegowanie dwoch argumentow z dowch parametrow. jesli jeden arg drugi ma miec domyslnie 2
def power(m,n=2):
    return m**n
print(power(3)) #9


#LAMBDA  lambda m,n=2 : m**n
def poower(n=3):
  return lambda m : m ** n
mydoubler = poower()

print(mydoubler(3)) #27
print(poower(3)) #<function poower.<locals>.<lambda> at 0x7f552a2d9940>

#####################################
two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

# The most interesting part of using lambdas appears when you can use them in their pure form - as anonymous parts of code intended to evaluate a result.
# The map() function applies the function passed by its first argument to all its second argument's elements, and returns an iterator delivering all subsequent function results.
#POTEGOWANIE POZIOM WYZEJ:

def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))
    
    
 

#An iterator is an object of a class providing at least two methods (not counting the constructor!):

#     __iter__() is invoked once when the iterator is created and returns the iterator's object itself;
#     __next__() is invoked to provide the next iteration's value and raises the StopIteration exception when the iteration comes to and end.



# The yield statement can be used only inside functions. The yield statement suspends function execution and causes the function to return the yield's argument as a result.
# Such a function cannot be invoked in a regular way – its only purpose is to be used as a generator (i.e. in a context that requires a series of values, like a for loop.)


# A list comprehension becomes a generator when used inside parentheses (used inside brackets, it produces a regular list). For example:
for x in (el * 2 for el in range(5)):
    print(x)


# A lambda function is a tool for creating anonymous functions.
def foo(x,f):
    return f(x)

print(foo(9, lambda x: x ** 0.5))


# 5. The map(fun, list) function creates a copy of a list argument, and applies the fun function to all of its elements, returning a generator 
# that provides the new list content element by element. For example:
short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)


# outputs ['Mython', 'Python', 'Fell', 'On', 'The', 'Floor'].

# 6. The filter(fun, list) function creates a copy of those list elements, which cause the fun function to return True. 
# The function's result is a generator providing the new list content element by element. For example:
short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)


# outputs ['Python', 'Monty'].

# 7. A closure is a technique which allows the storing of values in spite of the fact that the context in which they have been created does not exist anymore. For example:
def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]

    def inner(str):
        return tg + str + tg2
    return inner


b_tag = tag('<b>')
print(b_tag('Monty Python'))


# outputs <b>Monty Python</b>




any_list = [1, 2, 3, 4]
even_list = list(map(lambda n: n | 1, any_list))
print(even_list)

# lambdas should not be assigned to variables, but rather they should be defined as functions.

# This means that it is better to use a def statement, and avoid using an assignment statement that binds a lambda expression to an identifer. For example:
# Recommended:
def f(x): return 3*x
# Not recommended:
f = lambda x: 3*x



 
# Accessing files from Python code# Accessing files from Python code# Accessing files from Python code# Accessing files from Python code# Accessing files from Python code
# Accessing files from Python code# Accessing files from Python code# Accessing files from Python code# Accessing files from Python code
# Accessing files from Python code# Accessing files from Python code# Accessing files from Python code# Accessing files from Python code# Accessing files from Python code


            
            
            #zapis pliku 'r' 'w' - tworzy nowy plik jesli istnieje, czysci go 'a' - dopisuje do istniejacego pliku 
            # 'r+' read and write    na poczatku pliku 'w+' odczyt zapis, plik jest tworzony jesli nie istnieje i czysci istniejeacy
            # w+ open mode: write and update the stream will be opened in write and update mode;
            # 'a+'dopisuje na koniec pliku, jesli nie istnieje plik, tworzy go
# Text  Binary  Description
# rt 	rb 	    read
# wt 	wb 	    write
# at 	ab 	    append
# r+t 	r+b 	read and update
# w+t 	w+b 	write and update
with open('tajne_dane.txt', 'a') as tajne_dane:
    
    tajne_dane.write('mail@mail.com\n')
        
        
        
#odczyt pliku
with open('tajne_dane.txt', 'r') as tajne_dane:
    
    if tajne_dane.readable():
        for linijka in tajne_dane.readlines():
            if linijka[0] == '#':
                continue # w pliku poczatki linijek # beda pomijane
            print(linijka.lstrip())
            
from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))   
    
    
    
import errno

try:
    s = open("tzop.txt", "rt", encoding = "utf-8")
    print(s.read()) # printing the content of the file
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)
        
# Pre-opened streams:
# We said earlier that any stream operation must be preceded by the open() function invocation. There are three well-defined exceptions to the rule.
# When our program starts, the three streams are already opened and don't require any extra preparations. 
# What's more, your program can use these streams explicitly if you take care to import the sys module:


    # sys.stdin
    #     stdin (as standard input)
    #     the stdin stream is normally associated with the keyboard, pre-open for reading and regarded as the primary data source for the running programs;
    #     the well-known input() function reads data from stdin by default.

    # sys.stdout
    #     stdout (as standard output)
    #     the stdout stream is normally associated with the screen, pre-open for writing, regarded as the primary target for outputting data by the running program;
    #     the well-known print() function outputs the data to the stdout stream.

    # sys.stderr
    #     stderr (as standard error output)
    #     the stderr stream is normally associated with the screen, pre-open for writing, regarded as the primary place where
    # the running program should send information on the errors encountered during its work;
    #     we haven't presented any method to send the data to this stream (we will do it soon, we promise)
    #     the separation of stdout (useful results produced by the program) from the stderr (error messages, undeniably 
    # useful but does not provide results) gives the possibility of redirecting these two types of information to the different targets. 
    # More extensive discussion of this issue is beyond the scope of our course. The operation system handbook will provide more information on these issues.

#     This belief is only partly justified. If the stream was opened for writing and then a series of write operations were performed, it may happen that the data sent to the stream has not been transferred to the physical device yet (due to mechanism called caching or buffering).

#     Since the closing of the stream forces the buffers to flush them, it may be that the flushes fail and therefore the close() fails too.

# We have already mentioned failures caused by functions operating with streams but not mentioned a word how exactly we can identify the cause of the failure.

# The possibility of making a diagnosis exists and is provided by one of streams' exception component which we are going to tell you about just now.
# Diagnosing stream problems

# The IOError object is equipped with a property named errno (the name comes from the phrase error number) and you can access it as follows:
# try:
#     # Some stream operations.
# except IOError as exc:
#     print(exc.errno)


# The value of the errno attribute can be compared with one of the predefined symbolic constants defined in the errno module.

# Let's take a look at some selected constants useful for detecting stream errors:

#     errno.EACCES → Permission denied

#     The error occurs when you try, for example, to open a file with the read only attribute for writing.

#     errno.EBADF → Bad file number

#     The error occurs when you try, for example, to operate with an unopened stream.

#     errno.EEXIST → File exists

#     The error occurs when you try, for example, to rename a file with its previous name.

#     errno.EFBIG → File too large

#     The error occurs when you try to create a file that is larger than the maximum allowed by the operating system.

#     errno.EISDIR → Is a directory

#     The error occurs when you try to treat a directory name as the name of an ordinary file.

#     errno.EMFILE → Too many open files

#     The error occurs when you try to simultaneously open more streams than acceptable for your operating system.

#     errno.ENOENT → No such file or directory

#     The error occurs when you try to access a non-existent file/directory.

#     errno.ENOSPC → No space left on device

#     The error occurs when there is no free space on the media.

# The complete list is much longer (it includes also some error codes not related to the stream processing.)
from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
#OUT:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# Characters in file: 131
# Lines in file:      4
from os import strerror

try:
    fo = open('newtext.txt', 'wt')
    for i in range(10):
        fo.write("line #" + str(i+1) + "\n")
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))











from os import strerror

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) succesfully written')
src.close()
dst.close()









# Key takeaways

# 1. To read a file’s contents, the following stream methods can be used:

#     read(number) – reads the number characters/bytes from the file and returns them as a string; is able to read the whole file at once;
#     readline() – reads a single line from the text file;
#     readlines(number) – reads the number lines from the text file; is able to read all lines at once;
#     readinto(bytearray) – reads the bytes from the file and fills the bytearray with them;


# 2. To write new content into a file, the following stream methods can be used:

#     write(string) – writes a string to a text file;
#     write(bytearray) – writes all the bytes of bytearray to a file;


# 3. The open() method returns an iterable object which can be used to iterate through all the file's lines inside a for loop. For example:
# for line in open("file", "rt"):
#     print(line, end='')


# The code copies the file's contents to the console, line by line. Note: the stream closes itself automatically when it reaches the end of the file.






#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM
#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM
#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM#OPERATING SYSTEM

import os
print(os.uname()[2]) #release
    # systemname — stores the name of the operating system;
    # nodename — stores the machine name on the network;
    # release — stores the operating system release;
    # version — stores the operating system version;
    # machine — stores the hardware identifier, e.g., x86_64.


import os

os.makedirs("my_first_directory/my_second_directory") #Windows mkdir my_first_directory/my_second_directory
os.makedirs("my_first_directory/my_second_directory")  #Linux mkdir -p my_first_directory/my_second_directory
os.chdir("my_first_directory")
print(os.listdir())# ['my_second_directory']
print(os.getcwd())
os.rmdir("my_first_directory") #Deleting dir or  removedirs()
# As you’ve probably guessed, the os module provides a function that returns information about the current working directory.
# It's called getcwd. Look at the code in the editor to see how to use it in practice.

    # my_first_directory — this is a relative path which will create the my_first_directory directory in the current working directory;
    # ./my_first_directory — this is a relative path that explicitly points to the current working directory. It has the same effect as the path above;
    # ../my_first_directory — this is a relative path that will create the my_first_directory directory in the parent directory of the current working directory;
    # /python/my_first_directory — this is the absolute path that will create the my_first_directory directory, which in turn is in the python directory in the root directory.


import os

returned_value = os.system("mkdir my_first_directory")
 
print(returned_value)

# The system() function
# All functions presented in this part of the course can be replaced by a function called system, which executes a command passed to it as a string.
# The system function is available in both Windows and Unix. Depending on the system, it returns a different result.
# In Windows, it returns the value returned by the shell after running the command given, while in Unix, it returns the exit status of the process.
# Let's look at the code in the editor and see how it is in practice.
# Result:
# 0

# output
# The above example will work in both Windows and Unix. In our case, we receive exit status 0, which indicates success on Unix systems.
# This means that the my_first_directory directory has been created.


import os

os.mkdir("hello") # the relative path
os.mkdir("/home/python/hello") # the absolute path








# Introduction to the datetime module Introduction to the datetime moduleIntroduction to the datetime moduleIntroduction to the datetime moduleIntroduction to the datetime moduleIntroduction to the datetime moduleIntroduction to the datetime moduleIntroduction to the datetime module
# Introduction to the datetime moduleIntroduction to the datetime moduleIntroduction to the datetime moduleIntroduction to the datetime moduleIntroduction to the datetime module
# vIntroduction to the datetime moduleIntroduction to the datetime moduleIntroduction to the datetime moduleIntroduction to the datetime moduleIntroduction to the datetime module
# Introduction to the datetime moduleIntroduction to the datetime moduleIntroduction to the datetime moduleIntroduction to the datetime moduleIntroduction to the datetime module



# In this section, you'll learn about a Python module called datetime.

# As you can guess, it provides classes for working with date and time. If you think you don't need to delve into this topic, let's talk about examples of using date and time in programming.

# Date and time have countless uses and it's probably hard to find a production application that doesn't use them. Here are some examples:

#     event logging — thanks to the knowledge of date and time, we are able to determine when exactly a critical error occurs in our application. When creating logs, you can specify the date and time format;
#     tracking changes in the database — sometimes it's necessary to store information about when a record was created or modified. The datetime module will be perfect for this case;
#     data validation — you'll soon learn how to read the current date and time in Python. Knowing the current date and time, we're able to validate various types of data, e.g., whether a discount coupon entered by a user in our application is still valid;
#     storing important information — can you imagine bank transfers without storing the information of when they were made? The date and time of certain actions must be preserved, and we must deal with it.


from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp) #Timestamp: 1642698209.569788
d = date.fromtimestamp(timestamp)
print("Date:", d) #Date: 2022-01-20





from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)





from datetime import time

t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)
time.sleep(2)



# time(hour, minute, second, microsecond, tzinfo, fold)
# The time class constructor accepts the following optional parameters:
# Parameter 	Restrictions
# hour 	
# The hour parameter must be greater than or equal to 0 and less than 23.
# minute 	
# The minute parameter must be greater than or equal to 0 and less than 59.
# second 	
# The second parameter must be greater than or equal to 0 and less than 59.
# microsecond 	
# The microsecond parameter must be greater than or equal to 0 and less than 1000000.
# tzinfo 
# The tzinfo parameter must be a tzinfo subclass object or None (default).
# fold 	
# The fold parameter must be 0 or 1 (default 0).

import time

timestamp = 1572879180
print(time.ctime(timestamp)) #Mon Nov  4 14:53:00 2019
import time

timestamp = 1572879180
print(time.gmtime(timestamp))#time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
print(time.localtime(timestamp)) #time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
print(time.asctime(st)) #Mon Nov  4 14:53:00 2019
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0))) #1572879180.0


from datetime import datetime

dt = datetime(2019, 11, 4, 14, 53)

print("Datetime:", dt)#Datetime: 2019-11-04 14:53:00
print("Date:", dt.date())#Date: 2019-11-04
print("Time:", dt.time())#Time: 14:53:00
print("today:", datetime.today()) #2022-01-20 17:21:46.544697
print("now:", datetime.now()) #2022-01-20 17:21:46.544697
print("utcnow:", datetime.utcnow()) #2022-01-20 17:21:46.544697

    # today() — returns the current local date and time with the tzinfo attribute set to None;
    # now() — returns the current local date and time the same as the today method, unless we pass the optional argument tz to it. The argument of this method must be an object of the tzinfo subclass;
    # utcnow() — returns the current UTC date and time with the tzinfo attribute set to None.
dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp()) #Timestamp: 1601823300.0


d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d')) #2020/01/04


timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st)) #2019/11/04 14:53:00
print(time.strftime("%Y/%m/%d %H:%M:%S")) #2022/01/20 17:32:45
from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3) 
print(delta) #16 days, 3:00:00



# timedelta object only stores days, seconds, and microseconds internally. Similarly, the hour argument is converted to minutes. Take a look at the example below:
from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days) #Days: 16
print("Seconds:", delta.seconds) #Seconds: 10800
print("Microseconds:", delta.microseconds) #Microseconds: 0

 
import calendar
print(calendar.month(2020, 11))

 
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2020, 12)
import calendar
print(calendar.weekday(2020, 12, 24))
print(calendar.weekheader(3)) #Mon Tue Wed Thu Fri Sat Sun

print(calendar.isleap(2020)) #True
print(calendar.leapdays(2010, 2021))  # Up to but not including 2021. #3


    # calendar.Calendar – provides methods to prepare calendar data for formatting;
    # calendar.TextCalendar – is used to create regular text calendars;
    # calendar.HTMLCalendar – is used to create HTML calendars;
    # calendar.LocalTextCalendar – is a subclass of the calendar.TextCalendar class. The constructor of this class takes the locale parameter, which is used to return the appropriate months and weekday names.
    # calendar.LocalHTMLCalendar – is a subclass of the calendar.HTMLCalendar class. The constructor of this class takes the locale parameter, which is used to return the appropriate months and weekday names.

c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")
#0 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 0 

    # itermonthdates2 – returns days in the form of tuples consisting of a day of the month number and a week day number;
    # itermonthdates3 – returns days in the form of tuples consisting of a year, a month, and a day of the month numbers. This method has been available since version 3.7;
    # itermonthdates4 – returns days in the form of tuples consisting of a year, a month, a day of the month, and a day of the week numbers. This method has been available since Python version 3.7.
c = calendar.Calendar()

for data in c.monthdays2calendar(2020, 12):
    print(data)
# One of them is the monthdays2calendar method, which takes the year and month, and then returns a list of weeks in a specific month. 
# Each week is a tuple consisting of day numbers and weekday numbers. Look at the code in the editor.