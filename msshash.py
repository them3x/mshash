import hashlib, sys
from tqdm import tqdm
from getpass import getpass

help = "Usage: python "+sys.argv[0]+" <MODE> <TYPE> <WORDLIST or ASCII FOR ENCRYPT> <HASH FOR DECRYPT>\n\n\n-------MODE---------------\n-d          Decrypt hash\n-e          Encrypt ASCII\n-s          Encrypt ASCII Secricy mode\n\n-------TYPE---------------\nmd5         Enc\Dec in md5 hash\nsha256      Enc\Dec in sha256\n\n--------------------------"


def decrypt(help):
	try:
		wordw = open(sys.argv[2], 'r')
	except Exception as erro:
		if "Permission denied" in erro:
			print "Permission Denied !"
			exit(0)
		print "[!] WordList not found"
		exit(0)

	try:
		mode = sys.argv[3]
	except Exception as erro:
		print help
		exit(0)


	def dmd5(wordw):

		lines = wordw.readlines()
		for i in tqdm(lines):
			i = i.replace('\n', '')
                        w_hash = hashlib.md5(str(i)).hexdigest()

			if w_hash == sys.argv[4]:
				print "\n[!] Hash as been decrypted !\nResult for",sys.argv[4],"["+str(i.replace('\n', ''))+"]"
				exit(0)

		print "[!] Hash not decrypted :("
		exit(0)

	def dsha256(wordw):
                lines = wordw.readlines()
                for i in tqdm(lines):
                        i = i.replace('\n', '')
                        w_hash = hashlib.sha256(str(i)).hexdigest()

                        if w_hash == sys.argv[4]:
                                print "\n[!] Hash as been decrypted !\nRsulte for",sys.argv[4],"["+str(i.replace('\n', ''))+"]"
                                exit(0)

                print "[!] Hash not decrypted :("
                exit(0)


        if mode == "md5":
		try:
			md5 = sys.argv[4]

                except:
                        print help
                        exit(0)

		if len(md5) != 32:
			print "[X] Invalid MD5 hash"
			exit(0)

                dmd5(wordw)

        elif mode == "sha256":
                try:
                        sha = sys.argv[4]
                except:
                        print help
                        exit(0)

                if len(sha) != 64:
                        print "[X] Invalid SHA256 hash"
                        exit(0)

                dsha256(wordw)
        else:
                print help
                exit(0)

def encrypt(help):
        try:
                how = sys.argv[2]

        except Exception as erro:
                print help
                exit(0)


        if how == "md5":
                how = "md5"
        elif how == "sha256":
                how = "sha"
        else:
                print help
                exit(0)


        try:
                if how == "md5":
			try:
	                        hash = sys.argv[3]
			except:
				print help

                        result = hashlib.md5(str(hash))
                        print result.hexdigest()
                        exit(0)

                if how == "sha":
                        try:
                                hash = sys.argv[3]
                        except:
                                print help

                        result = hashlib.sha256(str(hash))
                        print result.hexdigest()
                        exit(0)
        except:
                exit(0)

        result = hashlib.sha256(str(hash))
        print result.hexdigest()

def sigilo(help):
	try:
		how = sys.argv[2]

	except Exception as erro:
		print help
		exit(0)


	if how == "md5":
		how = "md5"
	elif how == "sha256":
		how = "sha"
	else:
		print help
		exit(0)


	try:
		if how == "md5":
		        hash = getpass("MD5 CRYPTER > ")
		        result = hashlib.md5(str(hash))
		        print result.hexdigest()
		        exit(0)

		if how == "sha":
		        hash = getpass("SHA265 CRYPTER > ")
		        result = hashlib.sha256(str(hash))
		        print result.hexdigest()
		        exit(0)
	except:
		exit(0)

	result = hashlib.sha256(str(hash))
	print result.hexdigest()


try:
	mode = sys.argv[1]
	if mode == "-h" or mode == "--help":
		print help
		exit(0)

except Exception as erro:
	print help
	exit(0)

if mode == "-d":
	decrypt(help)

elif mode == "-e":
	encrypt(help)

elif mode == "-s":
	sigilo(help)

else:
	print help
