# EXERCISE 40 - Kiswanto_D #

class Song(object): #Create a class named Song
    def __init__(self, lyrics):
	self.lyrics = lyrics

    def sing_me_a_song(self):
	for line in self.lyrics:
	    print line

    def nyanyi(self):
	print self.lyrics

# Instantiate the Song Class with LIST
happy_bday = Song(["Happy birthday to you",
		   "I don't want to get sued",
		   "So I'll stop right there"])

# Instantiate again the Song Class with LIST
bulls_on_parade = Song (["They rally around tha family ya!",
			 "With pockets full of shells"])

# Calling the method (function) in class
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

# STUDY DRILLS 
# 2. Instantiace a variable
new_song = "Selamat ulang tahun kami ucapkan"
indo_song = Song(new_song)
indo_song.nyanyi()
