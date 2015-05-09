# EXERCISE 15 - Kiswanto_D #

# Module untuk input file
from sys import argv
script, filename = argv

# Fungsi open() untuk menmbuka file
txt = open(filename)

# Print formatting dan Print variable txt dengan fungsi read
print  "Here's your file %r:" % filename
print txt.read()

# Input file prompt
print "Type the filename again:"
file_again = raw_input("> ")

# variabel dengan fungsi open() + parameter file_again
txt_again = open(file_again)

print txt_again.read()

# STUDY DRILLS 
# 1. DONE but in bahasa
# 2. understand
# 3. 
