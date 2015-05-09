# EXERCISE 39 - Kiswanto_D

# Membuat Dictionary pemetaan provinsi ke singkatan.
states = {
    'Jawa Barat': 'Jabar',
    'Jawa Timur': 'Jatim',
    'Kalimantan Selatan': 'Kalsel',
    'DKI Jakarta': 'DKI',
    'Sumatra Utara': 'Sumut'
}

# Membuat Dictionary pemetaan Kota ke singkatan.
cities = {
    'Jabar': 'Bandung',
    'Jatim': 'Surabaya',
    'DKI': 'Jakpus'
}

# Menambah beberapa Key ke dictionary kota.
cities['Kalsel'] = 'Banjarmasin'
cities['Sumut'] = 'Medan'

# Print Values dari Dictionary Cities.
print '-' * 10
print "Jabar State has: ", cities['Jabar']
print "Jatim State has: ", cities['Jatim']

# Print Values dari Dictionary States
print '-' * 10
print "Jawa Barat's abbreviation is: ", states['Jawa Barat']
print "Kalimantan Selatan's abbreviation is: ", states['Kalimantan Selatan']

# Akses Values / Keys Dictionary dari Sebuah Values / Keys Dictionary.
print '-' * 10
print "Jawa Barat has: ", cities[states['Jawa Barat']]
print "DKI Jakarta has: ", cities[states['DKI Jakarta']]

# Looping Dictionary (States) jadi List 
print '-' * 10
for state, abbrev in states.items(): # Merubah Dictionary jadi sebuah list.
    print "%s is abbreviated %s" % (state, abbrev)

# Looping Dictionary (Cities) jadi List 
print '-' * 10
for abbrev, city in cities.items(): # Merubah Dictionary jadi List
    print "%s has the city %s" % (abbrev, city)

# Print Formatting dengan Dictonary 
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# Variable with Dictionary Access
state = states.get('Texas')

# Conditional Dictionary
if not state:
    print "Sorry, no Texas."

# Dictionary Access with 2 Argument
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
