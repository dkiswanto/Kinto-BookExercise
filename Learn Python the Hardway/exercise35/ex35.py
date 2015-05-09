# EXERCISE 35 - Kiswanto_D

# Add Module exit() to script
from sys import exit

# Function Gold Room Area
def gold_room():
    print "this room is full of gold. How much do you take?"

    # Prompt Take Gold
    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
	how_much = int(choice)
    else:
	dead("man, learn to type a number.")

    # Not Greedy Conditional ( <50 )
    if how_much < 50:
	print "Nice, you're not greedy, you win!"
	exit(0)
    else:
	dead("You greed bastard!") # Call the dead function

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
	choice = raw_input("> ")
	
	if choice == "take honey":
	    dead("The bear looks at you then slaps your face off.")
	elif choice == "taunt bear" and not bear_moved: # enter taunt bear while first time (bear_moved still false),
	    print "The bear has moved from the door. Yoy can go through it now"
	    bear_moved = True
	elif choice == "taunt bear" and bear_moved: # Enter taunt bear 2nd time and the bear piss off wkwkw
	    dead("The bear gets pissed off and chews your leg off.")
	elif choice == "open door" and bear_moved: # If you enter open door with variable bear_moved true
	    gold_room()    # Go the the gold room function
	else:
	    print "I got no idea what that means"

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He , it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
	start()
    elif "head" in choice:
	dead("Well that was tasty!")
    else:
	cthulhu_room()

def dead(why):
    print why, "Good Job!"
    exit(0)

def start():
    print "You are in a dark room"
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
	bear_room()
    elif choice == "right":
	cthulhu_room()
    else:
	dead("You stumble around the room until you starve")

start()
