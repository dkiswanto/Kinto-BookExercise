# EXERCISE 17 - Kiswanto_D #

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# The Process 
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit ENTER to continue, CTRL+C to abort."
raw_input(">?")

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

# STUDY DRILLS

# 1. Not see it
# 2. ?
# 3. Completed
# 4. Because the built in function "close()" 
# will close the file and save some memory resource
