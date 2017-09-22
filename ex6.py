# a variable that contains a string(text in double quotes) with a formatted variable (d as in decimal)
x = "There are %d types of people." % 10
# variable
binary = "binary"
# variable
do_not = "don't"
# a variable that contains a string(text in double quotes) with multiple formatted variables (s as in text String) that have variables which point back to lines 4&6
y = "Those who know %s and those who %s." % (binary, do_not)

# Displays the x variable on the screen
print x
# Displays the y variable on the screen
print y

# Displays a string that contains a formated variable (r is display no matter what (debugging)) that goes back to line 2
print "I said: %r." % x
# Displays a string that contains a formated variable (s as in text String) that goes back to line 8
print "I also said: '%s'." % y

# 21 and 22 are variables the first is a built in type and the second is a string that contains a formatted variable
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# 25 matches up the formatted variable in 22 with the variable built in type of "False" on 21
print joke_evaluation % hilarious

# 28 and 29 are simple text strings
w = "This is the left side of..."
e = "a string with a right side."

# This command concatenates the two strings together
print w + e
