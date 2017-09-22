########################################       KEYWORDS        ####################################################
########################################       Modules         ####################################################
# import - see "from"
import math
print math.pi, # the comma keeps whatever follows on the same line
# as - for import and giving the module a different name
import math as maththelongname
print maththelongname.pi,
# from - used for importing a specific function from a module ie "from sys import exit" this allows you to just call 
#        "exit" in the code, otherwise if you just used "import sys" you would have to call "sys.exit" in the code
#        everytime. The obvious advantage to just calling import sys would be if you use mutliple functions from the
#        sys module that you need to use.
from math import pi
print pi
###################################################################################################################
########################################       Functions       ####################################################
# def - creates new user-defined function. Functions are objects in which we organize our code.
# return - closely connected with a function definition. Return exits the function and returns a value.
def multiplier(x):
    return x * x
a = multiplier(5)
print a
# lambda(inline function) - creates a new anonymous function - not bound to a specific name.
for i in (1, 2, 3, 4, 5):
    a = lambda x: x * x
    print a(i),
print
# global - access variables defined outside functions
w = 15
def function():
    global x
    x = 45
function()
print x
###################################################################################################################
########################################  Boolean Expressions  ####################################################
# is - tests for object identity
print "pie" is "pie"
# not - negates a boolean value
print "pi" not in "pie"
print "pi" is not "pie"
# and - requires all boolean expressions to be met
print ("pie" is "pie") and ("pi" not in "pie")
# or - at least one boolean expression must be met
print ("pie" is "pie") or ("pi" not in "pie") 
###################################################################################################################
###########################################  Control Flow  ########################################################
# while - statements inside the while loop are executed until the expression evaluates to False
i = 0
while (i != 5):
    i += 1
    print i
# break - interrupts the cycle of a loop
import random
while (True):
    val = random.randint(1, 10)
    print val,
    if (val == 3):
        break
# continue - interrupts the current cycle, without jumping out of the whole cycle. New cycle will begin.
i = 0
while (i < 10):
    i += 1 #or i = i + 1
    if (i % 2) == 0:
        continue
    print i,
print
# if, elif, and else - determine which statements are going to be executed
name = "Paul"
if name == "John":
    print "Hello John."
elif name == "Paul":
    print "Hello Paul."
else:
    print "Hello"
# for - iterates over items of a collection in order that they appear in the container
lyrics = "Here we go 'round the Mulberry Bush"
for i in lyrics:
    print i,
print
# with - have two related operations that need to execute as a pair with a block of code inbetween. Will finish 2nd operation.
#with open('output.txt', 'w') as f:
#    f.write('Hi there!')
###################################################################################################################
############################################  Exceptions  #########################################################
# try - We try to read a films file. If no exception occurs, we print the contents of the file to the console.
# except - If we provided an incorrect file name an IOError exception is raised, then the except executes it's code.
# finally - The finally keyword is always executed in the end. We use it to clean up our resources.
f = None
try:
    f = open('films', 'r')
    for i in f:
        print i,
except IOError:
    print "Error reading file"
finally:
    if f:
        f.close()
# raise - create a user defined exception
class YesNoException(Exception):
    def __init__(self):
        print 'Invalid value'
#uncomment this line and comment the next line to see it work with a prompt#answer = raw_input("Type yes or no or else!!")
answer = 'yes'
if (answer != 'yes' and answer != 'no'):
    raise YesNoException
else:
    print 'Correct value'
###################################################################################################################
##############################################  Other  ############################################################
# print - prints strings and/or decimal numbers to the screen #print by itself does a linefeed
print "I've been multiplied 3 times!"" " * 3
print "\tI've been tabbed!"
# del - deletes objects
example = ['a', 'b', 'c', 'd', 'e', 'f']
del example[2]
print example
del example[2:]
print example
# pass - used as a temporary placeholder so ie a function will not break the code if it isn't complete
def iefunction():
    pass
# assert - used for debugging, it verifies that something is how it should be and will throw an exception if it isn't
# uncomment this line and comment the next one to see it work with a prompt#salary = int(raw_input("Enter a non-negative number, otherwise an exceptions is thrown")) #How to prompt for non-stringed numbers
salary = 1
assert salary > 0
# class - creates new user defined objects
class Square:
    def __init__(self, x):
        self.a = x
    def area(self):
        print self.a * self.a
sq = Square(12)
sq.area()
# exec - executes Python code dynamically
exec("for i in [1, 2, 3, 4, 5]: print i")
# in - used for comparisons; see boolean expressions keywords for other examples
print 4 in (2, 3, 5, 6)
print 5 in (2, 3, 5, 6)
for i in range(5):
    print i
# yield - used w/ generators; exits the generator and returns a value
def gen():
    x = 11
    yield x
it = gen()
print it.next()
###################################################################################################################


###########################################    DATA TYPES    ######################################################
# True - primitive data type
# False - primitive data type
male = False
male = bool(random.randint(0, 1))
if (male):
    print "We will name him John"
else:
    print "We will name her Victoria"
# None - non existent, not known or empty -- This example prints None
def function():
    pass
print function()
# strings - strings are created with single(') or double(") quotes on both ends
print 'ima string ' + "and ima string"
# numbers - numbers are just that, they don't need to be enclosed with quotes, otherwise they are treated as a string
print 399 + 234959 * 3394885
## str() - convert a number to a string
print "you are " + str(44) + " years old!"
## int() - convert string to integer
print int('10') + 20
## float() - convert a string to a floating point number
print float('22.33') + 22.55
## bool() - function converts the integers to boolean(True, False) values
print bool(True) 
print bool(False)
print bool("text") # True b/c there's something there
print bool("") # False b/c nothing there
print bool(' ') # True b/c there's a space there
print bool(0) # False 0 as opposed to 1
print bool() # False b/c nothing there
print bool(3) # True something there
print bool(None) # False b/c it represents nothing
# lists - lists are comma seperated and surrounded by square brackets ([])
name_list = ["Paul", "Casey"]
print name_list
###################################################################################################################


#########################################   STRING ESCAPE SEQUENCES   #############################################
# \\ - allows you to enter a backslash without going into string escape mode
print 'here is a backslash \\'
# \' - allows you to enter a single quote without ending the string
print 'well hello\'s'
# \" - allows you to enter a double quote without ending the string
print "well \"hello\""
# \a - still in place from olden days, plays system speaker today
print "here's a \a ascii bell"
# \b - backspace
print "the next word's\b\b\b\b\b\bbackspaced"
# \f - Formfeed
print "this is a \f form feed"
# \n - new line
print "hello\noooooo"
# \r - end of line return to beginning of line
print "   bbb\raaa"
# \t - horizontal tab
print "here comes a horizontal \ttab!"
# \v - vertical tab
print "here comes a vertical\vtab!"
###################################################################################################################


#######################################   STRING FORMATS   ########################################################
# %d - integer
print 'there are %d apples in the basket' % 5
# %i - integer
print 'im an integer %i' % 4
# %o - shows number in octal format
print "i'm octal %o" % (50)
# %u - Obsolete, same as %d
# %x - shows number in hexadecimal notation (lowercase)
print "i'm very hexidecimal %x" % (40)
# %X - shows number in hexadecimal notation (Uppercase)
# %e - shows number in scientific format (lowercase)
print "i'm scientific format %e" % (2)
# %E - shows number in scientific format (Uppercase)
# %f - float value (number with a decimal)
print "you're \"floating\" %f and she is %f tall" % (342.44, 432.67)
# %F - float value (number with a decimal) -- causes number to always have a decimal
# %g - Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.
print "you're floating in a different way %g" % 4
# %G - Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.  -- always have decimal and trailing zeros are not removed
# %c - single character works with string character or integer
print "here is a single character %c" % "c"
# %r - string similar to %s but different, more like raw
print "this is %r" % "raw"
# %s - string
print "i think i will be using %s one a lot" % ("this")
# %% - No argument is converted gives you a "%"
###################################################################################################################


##########################################      OPERATORS      ####################################################
# + - add
print 1 + 1
print "hello" + " " + "there"
# - - subtract or negative value
print 10 - 20
# * - multiply
print 5 * 6
# ** - power
print 2 ** 20
# / - divide
print 5 / 2
# % - Modulo -  finds the remainder of division of one number by another. 9 % 4, 9 modulo 4 is 1, because 4 goes into 9 twice with a remainder of 1
print 9 % 4
# < - strictly less than
print 4 > 4
# > - strictly greater than
print 4 < 4
# <= - less than or equal to
print 4 <= 4
# >= - greater than or equal to
print 4 >= 4
# == - equal to
print 4 == 4
# != or <> - not equal to
print 4 != 4
# ( ) - used in math equations to do these first, also used for functions, classes, objects, etc.
def print_function ():
    print (4 + 5 * 2) + 1
print_function()
# [ ] - used to define lists
listy = ["first", "second"]
print listy[1]
# { } - used to define a dictionary
d = {'One': 1, 'Two' : 2, 'Three' : 3 }
print d['Two'] # prints "2"
# @ - decorator !!add to me!!
# , - keeps whatever follows on the same line
print "for",
print "you"
# ; - treats the following as a new line
print "hello";print "hello"
# : - used for functions, also in dictionaries !!add to me!!
# . - objects !!add to me!!
# = - defining variables, functions, lists, dictionaries, etc.
# += - adds another value with the variable's value and assigns the new value to the variable
a = 2
print a
a += 1
print a
# -= - subtracts another value with the variable's value and assigns the new value to the variable
# *= - multiplies another value with the variable's value and assigns the new value to the variable
# /= -  divides another value with the variable's value and assigns the new value to the variable
# %= - modulos another value with the variable's value and assigns the new value to the variable
# **= - the power of another value with the variable's value and assigns the new value to the variable
a = 8
print a
a **= 8
print a
###################################################################################################################
