# 1. Avoid multiple inheritance at all costs, as it's too complex to be useful reliably. 
#   If you're stuck with it, then be prepared to know the class hierarchy and spend time 
#   finding where everything is coming from.
# 2. Use composition to package up code into modules that is used in many different 
#   unrelated places and situations.
# 3. Use inheritance only when there are clearly related reusable pieces of code that fit 
#   under a single common concept, or if you have to because of something you're using.
###########################  I N H E R I T A N C E  #####################################
# Is-a relationships, ie Child is-a Parent in the following example.
# Implicit Inheritance (Actions on the child imply an action on the parent.)
class Parent(object):

    def implicit(self):
        print "PARENT implicit()"
        
class Child(Parent):
    pass
    
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# Override Explicitly (Actions on the child override the action on the parent.)
class Parent(object):
    
    def override(self): 
        print "PARENT override()"
        
class Child(Parent):
    
    def override(self):
        print "CHILD override()"
        
dad = Parent()
son = Child()

dad.override()
son.override()

# Alter Before Or After (Actions on the child alter the action on the parent.)
class Parent(object):

    def altered(self):
        print "PARENT altered()"
        
class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
        
dad = Parent()
son = Child ()

dad.altered()
son.altered()

# Using super() with an __init__ from a Parent class
class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()
        

###########################  C O M P O S I T I O N  #####################################
# This is a has-a relationship, where Child has-a Other that it uses to get its work done.
print "\n\n"
class Other(object):

    def override(self):
        print "OTHER override()"
        
    def implicit(self):
        print "OTHER implicit()"
        
    def altered(self):
        print "OTHER altered()"
        
class Child(object):
    
    def __init__(self):
        self.other = Other()
        
    def implicit(self):
        self.other.implicit()
        
    def override(self):
        print "CHILD override()"
        
    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"
        
son = Child()

son.implicit()
son.override()
son.altered()
