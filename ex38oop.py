# - Extra Credit - Learn about OOP - Found this site: http://net.tutsplus.com/tutorials/python-tutorials/python-from-scratch-object-oriented-programming/

# Exercise 1 - Defining a class and then Introducing Instances(Objects) and member variables
#class pet:
#	number_of_legs = 0 # Variable of the pet class
#doug = pet() # Instance(or an "Object") of the pet class
#doug.number_of_legs = 4 
#print "Doug has %s legs." % doug.number_of_legs


# Exercise 2 - Introducing Logic
#class pet:
#    number_of_legs = 0
#    def sleep(self): # Method - A function inside of a class
#        print "zzz"
#doug = pet()
#doug.sleep()


# Exercise 3 - Introducing Data
#class pet:
#    number_of_legs = 0
#    def sleep(self):
#        print "zzz"
#    def count_legs(self):
#        print "I have %s legs" % self.number_of_legs
#doug = pet()
#doug.number_of_legs = 4
#doug.count_legs() # if we stop at this point it's an identical solution as exercise 1, but you can't easily add extra objects/instances
#nemo = pet()
#nemo.number_of_legs = 0
#nemo.count_legs()


# Exercise 4 - Introducing Class Inheritance (Titled "Some More Advanced Features" in the article)
class pet:
    number_of_legs = 0
    def sleep(self):
        print "zzz"
    def count_legs(self):
        print "I have %s legs" % self.number_of_legs
class dog(pet):
    def bark(self):
        print "Woof"
doug = dog()
doug.bark() # Works as expected b/c the bark method is in the dog class which doug is now an object/instance of.
doug.sleep() # This works because through the "pet" argument in defining the dog class we have now inherited all the methods and member variables of the pet class. In effect doug belongs to both the dog and pet class.
doug.number_of_legs = 4
doug.count_legs()
