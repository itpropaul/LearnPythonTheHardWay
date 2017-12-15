#modules
from sys import exit
import random

def new_line():
    print "\n"


#################   G A M E   D E S C R I P T I O N   ####################################
def game_description():
    """This is a Memory Game.
    
    The Goals of this game are as follows:
    -Ability to easily add/remove new words & definitions
    -Incorporate different ways of learning
        -Studies have shown that teaching the same thing different ways
         helps to make it stick
    -Randomize order of quiz questions
    -Have the ability in the game to create Word and Definition Files to be played
        -Treat these Word and Definition Files as modules that can be loaded from 
        within the game
            -This could be done two ways:Every new set of Word/Definition lists could be
            seperate functions within the same module/.py file(Leaning towards this, not as messy...,
            but still modular), or every new set of Word/Definition lists could be seperate modules/.py files
    -Try to incorporate as much as possible from what has been taught up to this point
    in "Learn Python The Hard Way". Also go back and redo/add to the game as I progress in the book
    -Back Me Up, Back Me Up, Back Me Up to DropBox
         
    Outline:
    1. Display Words and Definitions
    2. Quiz user via Multiple Choice
    3. Quiz user via Fill in the blank
    """
    print ('Type "help the hard way" to access the game description The Hard Way.\n'
          'Type "help" to access the game description the easy way.\n'
          'To go straight into the program press Enter')
    help = raw_input("> ")
    
    if help == ("help the hard way"):
        new_line()
        print ("Run the following commands in the Python interpreter for the game "
               "description:\nimport ex36\nhelp(ex36.game_description)")
        raw_input("\nPress Enter to Continue\n"
        "> ")
        game_description()       
    elif help == ("help"):
        new_line()
        print game_description.__doc__
        raw_input("\nPress Enter to Continue\n"
        "> ")
        game_description()
    else:
        start()
##########################################################################################


#################  I N T R O D U C T I O N  ##############################################  
def start():
    print "Welcome to the ever Expandable, Modular, and Most Importantly Fascinating Memory GAME GAMe GAme Game"
    print "1. Create, Edit, or Delete a Word Set."
    print "2. Plaaaayyyyy the Game!!!"
    print "3. Exit"
    choice = raw_input("> ")
    
    if choice == ("1"):
        game_editor()
    elif choice == ("2"):
        game()
    elif choice == ("3"):
        exit(0)    
    else:
        print "That is not an option. Please type 1, 2, or 3."
        start()
##########################################################################################



#########################  G A M E    E D I T O R  #######################################
# See game_description doc string for where/how I want the word/definition lists to stored    

words = []
definitions = []

def game_editor():
    print "1. Create New Word Set"
    print "2. Edit Existing Word Set"
    print "3. Delete Existing Word Set"
    print "4. Return to Previous Menu"
    
    choice = raw_input("> ")
        
    if choice == ("1"):
        game_editor_create()
    elif choice == ("2"):
        game_editor_edit()
    elif choice == ("3"):
        game_editor_delete()
    elif choice == ("4"):
        start()
    else:
        print "That is not an option. Please type 1, 2, 3, or 4."
        game_editor()
            
            
def game_editor_create():
    print "Game Editor Word Set Creator"
    print "Enter the name for the New Word Set."
    word_set_name = raw_input("> ")
    print '"%s" has been created. You will now enter words followed by their definitions.' % word_set_name
    print 'To finish creating a new list type "DONE" for the Word *and* Definition fields.'
    
    word = "not DONE"
    definition = "not DONE"
    while (word and definition != "DONE"):
        word = raw_input("Word> ")
        print word    
        words.append(word)
        
        definition = raw_input("Definition> ")
        print definition
        definitions.append(definition)
        
        print words
        print definitions
    
        if word and definition == "DONE":
            words.pop() #this pop and the next one take the "DONE" off the list :)
            definitions.pop() 
            game_editor()
    
    
def game_editor_edit():
    print "Game Editor Word Set Editor"

def game_editor_delete():
    print "Game Editor Word Set Deletor"

##########################################################################################




#########################  G A M E  ######################################################
# See game_description doc string for where/how I want the word/definition lists to stored
def game():
    bash_commands = ['pwd', 'print working directory', 'hostname', "my computer's network name", 'mkdir', 'make directory']
    print "Memory Game"
    pwd = bash_commands[0]
    #pwd_definition = pwd(cardinal number plus 1) #This idea has to do with having words and definitions in the same list
    #Another obvious way would be to have two lists and match up words with definitions by the cardinal number 
    #   ie pwd is at 0 on bash_commands and the defintion for pwd is at 0 on bash_commands_definitions **This is probably easier**
    print pwd
    
##########################################################################################    
    
game_description()    
