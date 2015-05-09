# EXERCISE 18 - Kiswanto_D

# scripts with argv                      
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# no arguments
def print_none():
    print "I got nothin'."


print_two("Dede Kiswanto","Si Keren")
print_two_again("Kiswanto","D")
print_one("First!")
print_none()

