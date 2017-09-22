name = 'Paul R. Masek'
age = 28 # not a lie
height = 78 # inches
weight = 186 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Blond'

height_centimeters = height * 2.54
weight_kilos = weight / 2.2

print "Let's talk about %s." % name
print "He's %d centimeters tall." % height_centimeters
print "He's %d kilos heavy." % weight_kilos
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_centimeters, weight_kilos, age + height_centimeters + weight_kilos)
