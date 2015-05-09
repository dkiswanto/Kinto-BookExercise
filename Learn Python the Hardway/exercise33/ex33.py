# EXERCISE 33 - Kiswanto_D

def while_loop(num):
# Create a variable for a container
    i = 0
    numbers = []

# Add elements to list with while-loop
    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

# Print the list
print "Type the max digit to insert into the list"
num = raw_input("> ")
while_loop(int(num))
