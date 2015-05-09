# EXERCISE 16 #

# Modul / Library Input
from sys import argv
script, filename = argv

# Keterangan Decision
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL+C (^C)/"
print "If you do want that, hit ENTER."

# Prompt Decision
raw_input("?")

# Opening & Truncate the file
print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate(filename)

# Input File 
print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# Overwrite the File
print "I'm going to write these to line the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Close the File
print "And finally, we close it."
target.close()

# STUDY DRILLS
# 6. Tidak usah karena string / option 'w' sudah bermakna overwrite / truncate
