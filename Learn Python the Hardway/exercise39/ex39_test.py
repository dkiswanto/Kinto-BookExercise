# EXERCISE 39 TEST FILE - Kiswanto_D

import hashmap

# create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Jawa Barat', 'Jabar')
hashmap.set(states, 'Jawa Timur', 'Jatim')
hashmap.set(states, 'Kalimantan Selatan', 'Kalsel')
hashmap.set(states, 'DKI Jakarta', 'DKI')
hashmap.set(states, 'Sumatra Utara', 'Sumut')

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'Jabar', 'Bandung')
hashmap.set(cities, 'Jatim', 'Surabaya')
hashmap.set(cities, 'DKI', 'Jakpus')

# add some more cities
hashmap.set(cities, 'Kalsel', 'Pangandaran')
hashmap.set(cities, 'Sumut', 'Medan')

# print out some cities
print '-' * 10
print "Jabar State has: %s" % hashmap.get(cities, 'Jabar')
print "Jatim State has: %s" % hashmap.get(cities, 'Jatim')

# print some states
print '-' * 10
print "Jawa Barat's abbreviation is: %s" % hashmap.get(states, 'Jawa Barat')
print "Kalimantan Selatan's abbreviation is: %s" % hashmap.get(states, 'Kalimantan Selatan')

# do it by using the state then cities dict
print '-' * 10
print "Jawa Barat has: %s" % hashmap.get(cities, hashmap.get(states, 'Jawa Barat'))
print "DKI Jakarta has: %s" % hashmap.get(cities, hashmap.get(states, 'DKI Jakarta'))

# print every state abbreviation
print '-' * 10
hashmap.list(states)

# print every city in state
print '-' * 10
hashmap.list(cities)

print '-' * 10
state = hashmap.get(states, 'Texas')

if not state:
  print "Sorry, no Texas."

# default values using ||= with the nil result
# can you do this on one line?
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
