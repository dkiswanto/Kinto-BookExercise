# EXERCISE 44 A - KISWANTO_D #

# Class Parent / Utama
class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

# Class Inheritance / Turunan
class Child(Parent):
    print "Child Inheritance"

# Instantiate Class
dad = Parent()
son = Child()

# Call the function implicit() in class
dad.implicit()
son.implicit()
