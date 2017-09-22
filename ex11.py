print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
    
testVar = raw_input("Ask user for something. ")

print "So testVar goes here -> %s" % testVar


fav_color = raw_input("What is your favorite color? ")
leastfav_color = raw_input("What is your least favorite color? ")

print "%s is your favorite color. And you hate %s" % (fav_color, leastfav_color)
