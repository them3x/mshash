import hashlib
import sys

from getpass import getpass


try:
        how = sys.argv[1]

except Exception as erro:
        print "\nUse python",sys.argv[0],"<HASH>\n\nHASHS:\n-m\tMD5\n-s\tSHA256\n\n"
        exit(0)


if how == "-m":
        how = "md5"
elif how == "-s":
        how = "sha"
else:
        print "\nUse python",sys.argv[0],"<HASH>\n\nHASHS:\n-m\tMD5\n-s\tSHA256\n\n"
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
