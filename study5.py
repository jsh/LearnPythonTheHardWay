name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height = height * 2.54
weight = 180 # lbs
weight = weight / 2.2
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
print "Let's talk about %r." % name
print "He's %r centimeters tall." % height
print "He's %r kilograms heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, ty to get it exactly right
print "If I add %r, %r, and %r I get %r." % (age, height, weight, age + height + weight)
