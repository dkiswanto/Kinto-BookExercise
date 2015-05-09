# EXERCISE 42 - Kiswanto_D #

# Kelas Utama/Induk (Main Class)
class Animal(object):
    pass

# Kelas Inheritance (Turunan)
class Dog(Animal):
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

# Kelas Utama
class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

# Kelas Inheritance (Turunan)
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

# Kelas Induk
class Fish(object):
    pass

# Kelas Inheritance
class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

# Create Object From Class (Instance)
rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan # Create ???\

frank = Employee("Frank", 120000)

frank.pet = rover # Create ???

# Calling a class

flipper = Fish()

crouse = Salmon()

harry = Halibut()
