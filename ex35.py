from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"
    
    next = raw_input("> ")
    if "0" in next or "1" in next or "2" in next or "3" in next or "4" in next\
    or "5" in next or "6" in next or "7" in next or "8" in next or "9" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
        
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy dirtbag!")
        
        
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    
    while True:
        next = raw_input("> ")
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif "taunt" in next and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif "taunt" in next and bear_moved:
            dead("The bear gets pissed and chews your leg off.")
        elif ("open" or "enter" in next) and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
            
            
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
        
        
def dead(why):
    print why, "Good job!"
    exit(0)
    
def start():
    print "You are in a dark room."
    print "There is a door to your left and right."
    print "Which one do you take?"
    
    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
        
        
start()