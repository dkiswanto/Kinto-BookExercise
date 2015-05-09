# EXERCISE 24 - KISWANTO_D #

# Print with single quotes practice
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# a Variabel with Paragraph with \t (tabs) and \n (newlines) formatting
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# Print the Poem Variable
print "--------------"
print poem
print "--------------"

# Print Variabel Operasi Aritmatika degan Formatting
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# Fungsi membuat variabel operasi matematika
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# Membuat Variabel dan pemanggilan fungsi dengan variabel tersebut
start_point = 10000
beans, jars, crates = secret_formula(start_point)

# Print Hasil Fungsi Tersebut
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# Print Pemanggilan Fungsi dengan Variabel yang baru.
start_point = start_point / 10
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

