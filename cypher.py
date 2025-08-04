import hashlib
import sys

class Cypher():

	def hashs(type, word):

		if type == "SHA256":
			sha256_hash = hashlib.sha256(word.encode()).hexdigest()
			print(f"SHA256: {sha256_hash}")

		elif type == "MD5":
			md5_hash = hashlib.md5(word.encode()).hexdigest()
			print(f"MD5: {md5_hash}")

		elif type == "SHA512":
			sha512_hash = hashlib.sha512(word.encode()).hexdigest()
			print (f"SHA512: {sha512_hash}")

		elif type == "CAESAR":
			Cypher.caesar("-e", word)


	def chash(wordlist, hash, hash_to_crack, count):
		if hash == "SHA256":
			for word in wordlist:
				crack = word
				for n in range(count):
					crack = hashlib.sha256(crack.encode()).hexdigest()
					if crack == hash_to_crack:
						print ("Encontrado [ " + "SHA256("*(n+1) + word + ") ]\n\n")
						sys.exit(0)
		elif hash == "MD5":
			for word in wordlist:
				crack = word
				for n in range(count):
					crack = hashlib.md5(crack.encode()).hexdigest()
					if crack == hash_to_crack:
						print ("Encontrado [ " + "MD5("*(n+1) + word + ") ]\n\n")
						sys.exit(0)
		elif hash == "SHA512":
			for word in wordlist:
				crack = word
				for n in range(count):
					crack = hashlib.sha512(crack.encode()).hexdigest()
					if crack == hash_to_crack:
						print ("Encontrado [ " + "SHA512("*(n+1) + word + ") ]\n\n")
						sys.exit(0)


	def caesar(mode, keyw):

		if mode == "-d":
			dec = True

		elif mode == "-e":
			dec = False

		def run(key, keyw, dec):
			print("\n["+str(key)+"]\t", end="")
			for i in keyw:
				if i == "a":
					alphabet = ["b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "a", "b"]
					old = ["b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "a", "b"]

					if dec == True:
						alphabet = []
						for i in range(26, 0, -1):
							alphabet.append(old[i])
						alphabet.append(old[0])

					count = 0
					for i in alphabet:
							count += 1
							if key == count:
								print(i, end="")
								break

				elif i == "b":
					alphabet = ["c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a", "b", "c"]
					old = ["c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c"]

					if dec == True:
						alphabet = []
						for i in range(26, 0, -1):
							alphabet.append(old[i])
						alphabet.append(old[0])

					count = 0
					for i in alphabet:
						count += 1

						if key == count:
							print(i, end="")
							break


				elif i == "c":
						alphabet = ["d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b", "c", "d"]
						old = ["d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b", "c", "d"]


						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "d":
						alphabet = ["e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c", "d", "e"]
						old = ["e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c", "d", "e"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):

								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "e":
						alphabet = ["f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f"]
						old = ["f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "f":
					alphabet = ["g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g"]
					old = ["g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g"]

					if dec == True:
						alphabet = []
						for i in range(26, 0, -1):
							alphabet.append(old[i])
						alphabet.append(old[0])

					count = 0
					for i in alphabet:
						count += 1

						if key == count:
							print(i, end="")
							break

				elif i == "g":
						alphabet = ["h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f", "g","h"]
						old = ["h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "h":
						alphabet = ["i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i"]
						old = ["i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "i":
						alphabet = ["j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j"]
						old = ["j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "j":
						alphabet = ["k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k"]
						old = ["k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "k":
						alphabet = ["l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l"]
						old = ["l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "l":
						alphabet = ["m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
						old = ["m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "m":
						alphabet = ["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
						old = ["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "n":
						alphabet = ["o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","0"]
						old = ["o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]


						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "o":
						alphabet = ["p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
						old = ["p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break


				elif i == "p":
						alphabet = ["q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"]
						old = ["q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "q":
						alphabet = ["r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
						old = ["r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1
							if key == count:
								print(i, end="")
								break

				elif i == "r":
						alphabet = ["s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]
						old = ["s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "s":
						alphabet = ["t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t"]
						old = ["t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t"]


						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "t":
						alphabet = ["u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u"]
						old = ["u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "u":
						alphabet = ["v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v"]
						old = ["v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "v":
						alphabet = ["w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]
						old = ["w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "w":
						alphabet = ["x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]
						old = ["x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):

								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "x":
						alphabet = ["y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]
						old = ["y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "y":
						alphabet = ["z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
						old = ["z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

						if dec == True:
						   alphabet = []
						   for i in range(26, 0, -1):
						   		alphabet.append(old[i])
						   alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break

				elif i == "z":
						alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a"]
						old = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a"]

						if dec == True:
							alphabet = []
							for i in range(26, 0, -1):
								alphabet.append(old[i])
							alphabet.append(old[0])

						count = 0
						for i in alphabet:
							count += 1

							if key == count:
								print(i, end="")
								break
				elif i == " ":
					print(" ", end="")




		for i in range(1, 27):
			run(i, keyw, dec)

		print ("\n\n")


