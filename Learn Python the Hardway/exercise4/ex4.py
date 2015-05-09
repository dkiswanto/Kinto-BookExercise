#EXERCISE 4 - Kiswanto_D#

cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#STUDY DRILLS#
#1. Yang terjadi jika salah satu variabel mengandung floating point dan 
#dioperasikan dengan variabel integer maka akan menghasilkan variabel floating point.

print "Hey %s there." % "you"
