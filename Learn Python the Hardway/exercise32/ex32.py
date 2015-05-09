# EXERCISE 32 - Kiswanto_D

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# looping for-loop pada sebuah list
for number in the_count:
    print "This is count %d" % number

# sama seperti diatas
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# looping pada mixed list
for i in change:
    print "I got %r" % i

# menocoba untuk membuat sebuah list dengan looping
# buat list kosong
elements = []

# gunakan looping dengan fungsi range()
# dan menambahkannya pada list
for i in range(0,6):
    print "Adding %d to the list." % i
    elements.append(i) #list.append() adalah fungsi untuk menambahkan index pada list

# print semua element pada list
for i in elements:
    print "Element was: %r" % i


# STUDY DRILLS
#1. built in fungsi range() sudah dipahami,
#2. Completed and of course it can
#3. COmpleted
