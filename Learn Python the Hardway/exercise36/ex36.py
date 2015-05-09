# EXERCISE 36 - Game Mencari Sang OSHI by Kiswanto_D

from sys import exit

def start():
	print """
	#### WOTA MENCARI OSHI ####
	"""
	raw_input("Enter untuk Play")

	print """
	--- Selamat Datang the Theater JKT48 ---
	--- Cobalah untuk mencari oshi anda ---
	"""
	print "Anda sedang sudah masuk ke dalam gedung"
	print "apa yang akan anda lakukan??"
	print " '1 = Berteriak menyuarakan oshi anda' "
	print " '2 = Terus jalan menyelusuri ruangan' "
	
	start = raw_input("> ")
	if start == "1":
		end("Banyak WOTA Langsung menyerbu")
	elif start == "2":
		lvl1()
	else:
		end(start)

def end(ket):
	print ket,	"dan anda berkakhir di RS Cipto Mangunkusumo"
	print """
	----------------------------------------------------
	Apakah anda masih ingin berjuang mencari oshi anda?
	"""
	print "ya/tidak"
	berjuang = raw_input("> ")
	if berjuang == "ya":
		start()
	elif berjuang == "tidak":
		exit(0)
	else:
		print "Mungkin anda lelah, sudah tidur sana nak!!"
		exit(0)

def lvl1():
	print "kamu menemukan sebuah pintu"
	print "untuk masuk ke pintu tersebut kamu harus menjawab sebuah pertanyaan"
	print "Siapakah memeber termuda JKT48 Gen1??"
	quest_level1 = ""
	while quest_level1 != "nabilah":
		quest_level1 = raw_input("> ")
		if quest_level1 == "nabila":
			print "mungkin maksud anda nabilah?"
			print "Please try again"
		elif quest_level1 == "nabilah":
			print "Jawaban Benar, pintu terbuka"
			lvl2()
		elif quest_level1 == 'aku ingin pulang':
			end("anda tidak selamat karena digebukin WOTA dijalan")
		else:
			print "Coba lagi, masukan 'aku ingin pulang' / atau tekan CTRL+C untuk keluar "

def lvl2():

	print "disini kamu memasuki ruangan yang sangat besar dan melihat ada 5 pintu"
	print "pilih dan bukalah pintu tersebut"
	pintu = [1,2,3,4,5]
	print pintu

	quest_level2 = 99
	while quest_level2 != 0:
		quest_level2 = int(raw_input("> "))
		if quest_level2 == 1:
			print "tidak ada adapaun kamar yang kosong"
		elif quest_level2 == 2:
			print "tidak ada adapaun kamar yang kosong"
		elif quest_level2 == 3:
			print "tidak ada adapaun kamar yang kosong"
		elif quest_level2 == 4:
			print "Bencong menarik anda dari pintu tersebut dan meng-IYKWIM kamu secara paksa!!"
			print "sampai kamu serangan jantung dan meninggal!!"
			print "GAME OVER"
			exit(0)
		elif quest_level2 == 5:
			print """
			HORE SELAMAT ANDA KETEMU OSHI ANDA
			SEBAGAI BALASAN KARENA TELAH MENYELAMATKAN OSHI ANDA
			ANDA MENDAPATKAN HANDSHAKE GRATIS WKWKW
			"""
			raw_input("Tekan Enter untuk Credit")
			print "Games by Kiswanto_D"
			print """
			----------------------------------------------------
			Apakah anda ingin bermain lagi??
			"""
			print "ya/tidak"
			main_lagi = raw_input("> ")
			if main_lagi == "ya":
				start()
			elif main_lagi == "tidak":
				exit(0)
			else:
				print "Mungkin anda lelah, sudah tidur sana nak!!"
			exit(0)
		
		else:
			print "Anda Harus memilih pintu!!!!!"

start()