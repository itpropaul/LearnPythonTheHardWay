# Allows you to add arguments to the script - they are space delimited and the first one is a given the script name so in this case the script only needs one argument added after the script name to run and it will be referred to as "filename" in the script
from sys import argv

# As i said on line 1 the first part of this argument variable is alwasy the script name. Filename is the variable that is equal to what you enter after typing python ex15.py 
script, filename = argv

# Variable txt is telling python to open the file
txt = open (filename)

# Displays the name of the file that we just opened on line 8
##print "Here's your file %r:" % filename
# Run a .read() function on the txt variable which opens the file specified in the argument variable up on lines 2 and 5
print txt.read()

# Displaying text to the user
##print "Type the filename again:"
# This is doing the same thing as before but instead of grabbing the text file via an argument after the script name in bash it interactively asks for it after the script has begun. So the name of the file now equals the variable name of file_again
##file_again = raw_input("> ")

# see line 7
##txt_again = open(file_again)

# see line 12
##print txt_again.readline()
##print txt_again.readline()
##print txt_again.readline()

txt.close()
##txt_again.close()
