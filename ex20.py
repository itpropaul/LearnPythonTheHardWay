# Grab argv function(or feature as Zed calls it) from the sys package
from sys import argv

# argv command which grabs arguments from the command line, in this case just one as script(equals the script file name) is a given
script, input_file = argv

# Tiny function to take input f and print out it's contents
def print_all(f):
    print f.read()
    
# Small function to go back to the original byte of the file. I tried running the above command two times without this rewind command and the second time it came out blank, so this is definitely needed. As Zed explains Python treats input files as tape player would treat a tape. If you have played through the tape like we did with the original command, you have to rewind it to play it again.
def rewind(f):
    f.seek(0)
    
# This function prints out a single line from a file. It also displays which line it's on before displaying the line. The comma at the end of line 17 was added to avoid the unnecessary spacing between the following lines that were printed to the screen.
def print_a_line(line_count, f):
    print line_count, f.readline(),
    
# Variable that open's an input file. The input file was originally grabbed from the command line on line 2 and 5.
current_file = open(input_file)

# Displays text and adds a new line with an escape sequence.
print "First let's print the whole file:\n"

# Runs print_all function and inputs the current_file which opens the input_file which was pulled from argv(argument variable)
print_all(current_file)

# Displays text
print "Now let's rewind, kind of like a tape."

# Calls up the rewind function
rewind(current_file)

# Displays text
print "Let's print three lines:"


# Runs print_a_line function and keeps adding one to current line making the current line variable increase by one every time.
# Current_Line = 1
current_line = 1
print_a_line(current_line, current_file)

# Current_Line = 2
current_line += 1
print_a_line(current_line, current_file)

# Current_Line = 3
current_line += 1
print_a_line(current_line, current_file)
