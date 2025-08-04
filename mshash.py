#encoding: utf8

'''
GNU GENERAL PUBLIC LICENSE

Version 3, 29 June 2007

Copyright © 2007 Free Software Foundation, Inc. <http s ://fsf.org/>
'''
#encoding: UTF-8

import getpass
import argparse
import os
import sys
import threading
from cypher import Cypher

parser = argparse.ArgumentParser(description='Exemplo de uso do argparse.')
parser.add_argument('command', choices=['e', 'b', 'd'], help='e = encripta / b = brute force / d = decodificar')
parser.add_argument('hash_type', choices=['sha256', 'sha512', 'md5', 'caesar'], help='Obrigatório, deve ser sha256, sha512, md5 ou caesar')
parser.add_argument('input', nargs='?', default=None, help='opcional para "e"')
parser.add_argument('wordlist', nargs='?', default=None, help='Wordlist')
parser.add_argument('hash_time', nargs='?', default=None, help='Numero de voltas. default=1')

args = parser.parse_args()

if args.command == 'b':
	if args.input is None:
		parser.error('Especifique a hash alvo')

	if args.wordlist is None:
		parser.error('Especifique a wordlist')
	else:
		if os.path.isfile(args.wordlist) == False:
			print ("Arquivo [ " + args.wordlist + " ] não existe")
			sys.exit(0)

	if args.hash_time is None:
		count = 1
	else:
		count = int(args.hash_time)

	hash_t = args.hash_type.upper()
	print ("Hash alvo: " + args.input)
	print ("Tipo: " + hash_t)
	print ("Voltas: " + str(count))

	with open(args.wordlist, encoding='ISO-8859-1') as wordlist:
		words = []
		for word in wordlist.readlines():
			word = word.replace('\n', '')
			words.append(word)

		lwords = len(words)
		first = lwords // 3
		second = 2 * first

		lst1 = words[:first]
		lst2 = words[first:second]
		lst3 = words[second:]

		print ("Wordlist: " + args.wordlist + " | (" + str(lwords) + ") Palavras / 3 Sub WordList's")
#		print ("Sub W1 (" + str(len(lst1)) + ") Palavras")
#		print ("Sub W2 (" + str(len(lst2)) + ") Palavras")
#		print ("Sub W3 (" + str(len(lst3)) + ") Palavras")
		print ("\nTrabalhando...\n\n")

		if hash_t == "SHA256":
			thread1 = threading.Thread(target=Cypher.chash, args=(words, hash_t, args.input, count))
			thread1.start()

		elif hash_t == "SHA512":
			thread1 = threading.Thread(target=Cypher.chash, args=(words, hash_t, args.input, count))
			thread1.start()

		elif hash_t == "MD5":
			thread1 = threading.Thread(target=Cypher.chash, args=(words, hash_t, args.input, count))
			thread1.start()



elif args.command == "e":
	type = args.hash_type.upper()

	if args.input is None:
		word = getpass.getpass("Digite: ")
	else:
		word = args.input

	Cypher.hashs(type, word)

elif args.command == "d":
	word = args.input
	if args.hash_type.upper() == "CAESAR":
		Cypher.caesar("-d", word)
