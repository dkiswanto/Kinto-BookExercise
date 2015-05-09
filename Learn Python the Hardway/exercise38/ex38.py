# EXERCISE 38 - Kiswanto_D

# Make variable with string
ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ') # Make variable string to variable list
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girls", "Boy"] # Create another list

while len(stuff) != 10:
    next_one = more_stuff.pop() # pop 1 element in list
    print "Adding: ", next_one
    stuff.append(next_one) # add / push 1 element in list
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

# Play with List
print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
