# This is a function that has two arguments. It prints four lines, the first two contain formatted variables(%d for decimal(numbers)) and the fourth contains an escape sequence.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"
    
    
# Line 11 is calling the function and inputing two numbers directions
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


# Lines 16-19 create two new variables and then the function is called and it inputs the variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# This is another example of directly inputing numbers but they are math equations
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# This combines variables with math equations
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
