#encoding: utf8

'''
GNU GENERAL PUBLIC LICENSE

Version 3, 29 June 2007

Copyright © 2007 Free Software Foundation, Inc. <http s ://fsf.org/>
'''

import hashlib, sys, os
from getpass import getpass

help = """--| Avaliable MODEs |--
base64\t\t -e<d> base64 teste123
md5\t\t -e<d> md5 test123 </usr/share/wordlist/passmd5.txt> | Encode/Break MD5
sha256\t\t -e<d> sha256 test123 </usr/share/wordlist/pass256.txt> | Encode/Break SHA256
cipher caesar\t -e<d> caesar test123 [1/24 - a] | Encode/Decode on cipher caesar
overutf8\t -e payload123 | Encode on overload UTF-8

----------------------

Use "mshash -e md5/sha256 sec" not to show the keyword (security mode)

"""
try:
	if sys.argv[1] == "--help" or sys.argv[1] == "-h":
		print help
except:
	None

try:
	mode = str(sys.argv[1])
	cripto = str(sys.argv[2])
	data = str(sys.argv[3])

	try:
		wordlist = str(sys.argv[4])
	except:
		wordlist = False
except:
	print "Use: python",sys.argv[0],"<MODE> <TYPE> <YOUR PLAIN/ENCRYPTED ASCII> <WORDLIST>"
	exit(0)

def b64(code, mode):
	if mode == "-e":
		print "-"*15,"\nENCRYPT|BASE 64\n","-"*15

		value = code.encode('base64')
		print "-"*6,"\nRESULT\n","-"*6,"\n\n",value
		print "-"*20
		exit(0)

	elif mode == "-d":
		print "-"*15,"\nDECRYPT|BASE 64\n","-"*15
		try:
		        valor = code.decode('base64')
		except:
		        print "[!] Appending [=] to code"

		        try:
		                code += "="
		                valor = code.decode('base64')
		        except:
		                print "[!] Trying [==] on the code"

		                try:
		                        code += "="
		                        valor = code.decode('base64')
		                except Exception as error:
		                        print "[X] Fatal error:", error
		                        exit(0)

		print "-"*6,"\nRESULT\n","-"*6,"\n"
		print valor
		print "\n","-"*20

	else:
		print "Unknow mode ["+str(mode)+"]"
		exit(0)


def md5(data, mode, wordlist):
	if mode == "-e":
                print "-"*11,"\nENCRYPT|MD5\n","-"*11

		if data == "sec":
			data = getpass("Password: ")

	        result = hashlib.md5(data)
		print "-"*6,"\nRESULT\n","-"*6,"\n\n"
	        print result.hexdigest()
		print "\n","-"*len(result.hexdigest())
		exit(0)

	elif mode == "-d":
                print "-"*11,"\nDECRYPT|MD5\n","-"*11

		if len(data) != 32:
			print data,"is not a MD5 hash"
			exit(0)
		print "Hash:",data

	        if os.path.isfile(wordlist):
			file = open(wordlist, 'r')
		else:
			print "Wordlist not fount :("
			exit(0)
		print "Wordlist:",wordlist
		size = len(file.readlines())
		print "Words in wordlist: "+str(size)
		file.close()
		file = open(wordlist, 'r')
		count = 0
		porcent = 10

		sys.stdout.write("Loading [%s]" % (" " * 10))
		sys.stdout.flush()
		sys.stdout.write("\b"* (10))
		for i in file.readlines():
			i = i.replace('\n', '')
			hash = hashlib.md5(i).hexdigest()
			math = size*porcent/100
			if count == math:
				sys.stdout.write("-")
				sys.stdout.flush()
	                        porcent += 10

			if hash == data:
				print "\nFound - "+str(i)
				exit(0)

			count += 1
		print "\nHash not fond :(\n"

def sha256(data, mode, wordlist):
        if mode == "-e":
                print "-"*14,"\nENCRYPT|SHA256\n","-"*14

                if data == "sec":
                        data = getpass("Password: ")

                result = hashlib.sha256(data)
                print "-"*6,"\nRESULT\n","-"*6,"\n\n"
                print result.hexdigest()
                print "\n","-"*len(result.hexdigest())
                exit(0)

        elif mode == "-d":
                print "-"*14,"\nDECRYPT|SHA256\n","-"*14

                if len(data) != 64:
                        print data,"is not a SHA265 hash"
                        exit(0)
                print "Hash:",data

                if os.path.isfile(wordlist):
                        file = open(wordlist, 'r')
                else:
                        print "Wordlist not fount :("
                        exit(0)
                print "Wordlist:",wordlist
                size = len(file.readlines())
                print "Words in wordlist: "+str(size)
                file.close()
                file = open(wordlist, 'r')
                count = 0
                porcent = 10

                sys.stdout.write("Loading [%s]" % (" " * 10))
                sys.stdout.flush()
                sys.stdout.write("\b"* (10))
                for i in file.readlines():
                        i = i.replace('\n', '')
                        hash = hashlib.sha256(i).hexdigest()
                        math = size*porcent/100
                        if count == math:
                                sys.stdout.write("-")
                                sys.stdout.flush()
                                porcent += 10

                        if hash == data:
                                print "\nFound - "+str(i)
                                exit(0)

                        count += 1
                print "\nHash not fond :(\n"


def caesar(key, mode, keyw):

        if mode == "-d":
                dec = True

        elif mode == "-e":
                dec = False

        else:
                print "Invalid Operation"
                exit(0)

        if key == "a" or key == "A":
                all = True

        else:
                all = False
                key = int(key)
                if key > 24:
                        print 'The key must be [1/24]'
                        exit(0)


	def run():
	        sys.stderr.write("\n["+str(key)+"]\t")
		for i in keyw:
			if i == "a":
				alphabet = ["b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
			        old = ["b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

				if dec == True:
					alphabet = []
					for i in range(24, 0, -1):
						alphabet.append(old[i])
			                alphabet.append(old[0])

			        count = 0
				for i in alphabet:
			                    count += 1
			                    if key == count:
			                            sys.stderr.write(i)
			                            break

			elif i == "b":
				alphabet = ["c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a"]
			        old = ["c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a"]

			        if dec == True:
			                alphabet = []
			                for i in range(24, 0, -1):
			                        alphabet.append(old[i])
			                alphabet.append(old[0])

				count = 0
				for i in alphabet:
					count += 1

					if key == count:
						sys.stderr.write(i)
			                        break


			elif i == "c":
				    alphabet = ["d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b"]
				    old = ["d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b"]


				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "d":
				    alphabet = ["e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c"]
				    old = ["e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "e":
				    alphabet = ["f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d"]
				    old = ["f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "f":
				    alphabet = ["g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e"]
				    old = ["g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "g":
				    alphabet = ["h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f"]
				    old = ["h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "h":
				    alphabet = ["i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g"]
				    old = ["i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "i":
				    alphabet = ["j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h"]
				    old = ["j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "j":
				    alphabet = ["k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i"]
				    old = ["k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "k":
				    alphabet = ["l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j"]
				    old = ["l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "l":
				    alphabet = ["m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k"]
				    old = ["m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "m":
				    alphabet = ["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l"]
				    old = ["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "n":
				    alphabet = ["o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
				    old = ["o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]


				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "o":
				    alphabet = ["p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
				    old = ["p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				    	count += 1

				        if key == count:
				            	sys.stderr.write(i)
				                break


			elif i == "p":
				    alphabet = ["q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]
				    old = ["q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "q":
				    alphabet = ["r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
				    old = ["r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1
				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "r":
				    alphabet = ["s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"]
				    old = ["s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "s":
				    alphabet = ["t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
				    old = ["t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]


				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "t":
				    alphabet = ["u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]
				    old = ["u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "u":
				    alphabet = ["v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t"]
				    old = ["v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "v":
				    alphabet = ["w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u"]
				    old = ["w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "w":
				    alphabet = ["x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v"]
				    old = ["x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "x":
				    alphabet = ["y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]
				    old = ["y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "y":
				    alphabet = ["z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]
				    old = ["z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]


				    if dec == True:
				           alphabet = []
				           for i in range(24, 0, -1):
				           		alphabet.append(old[i])
				           alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break

			elif i == "z":
				    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]
				    old = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]

				    if dec == True:
				            alphabet = []
				            for i in range(24, 0, -1):
				                    alphabet.append(old[i])
				            alphabet.append(old[0])

				    count = 0
				    for i in alphabet:
				            count += 1

				            if key == count:
				                    sys.stderr.write(i)
				                    break
			elif i == " ":
				sys.stderr.write(" ")



	if all == True:
	        for i in range(1,25):
	                key = i
	                run()
	        print "\n\n"

def overutf8(data):
	payload = data
	print "-"*22,"\nENCRYPT|OVERLONG UTF-8\n","-"*22
	print "-"*6,"\nRESULT\n","-"*6,"\n\n"
	for data in payload:
		sys.stderr.write("%%%.2X%%%.2X" % (0xc0 + (ord(data) >> 6), 0x80 + (ord(data) & 0x3f)))
	print '\n'+"-"*20

if cripto == "b64" or cripto == "B64" or cripto == "base64" or cripto == "BASE64":
	b64(data, mode)

elif cripto == "md5" or cripto == "MD5":
	md5(data, mode, wordlist)

elif cripto == 'sha256' or cripto == 'SHA256':
	sha256(data,mode,wordlist)

elif cripto == "caesar":
	caesar(wordlist, mode, data)
elif cripto == "overutf8":
	overutf8(data)
