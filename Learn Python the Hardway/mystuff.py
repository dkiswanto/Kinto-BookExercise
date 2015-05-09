class Parent(object):
    def implicit(self):
        print "PARENT implicit()"
class Child(Parent):
    print "something"

#dad = Parent()
son = Child()

#dad.implicit()
son.implicit()
