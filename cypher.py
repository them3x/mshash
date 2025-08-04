from Crypto.Hash import MD2, MD4
from Crypto.Hash import KMAC128, KMAC256
from Crypto.Hash import keccak
from Crypto.Hash import RIPEMD160
from passlib.hash import phpass
from passlib.hash import bcrypt_sha256
from lang import invalidHash_en, invalidHash_ptBR
import getpass
import sys
import hashlib
import base64

class Cypher():
    def hashs(types, word, lang):
        used = ""

        for type in types:
            type = type.upper()
            used = f"{type}({used})"

        # a ordem reversa simula a sintaxe em programação md5(sha512(texto))
        for type in types:
            type = type.upper()


            if type in ("MD2", "MD4", "MD5"):
                md_funcs = {
                    "MD2": lambda w: MD2.new(w.encode()).hexdigest(),
                    "MD4": lambda w: MD4.new(w.encode()).hexdigest(),
                    "MD5": lambda w: hashlib.md5(w.encode()).hexdigest()}

                word = md_funcs[type](word)

            # SHA2
            elif type in ("SHA1", "SHA224", "SHA256", "SHA384", "SHA512"):
                sha_funcs = {
                    "SHA1": hashlib.sha1,
                    "SHA224": hashlib.sha224,
                    "SHA256": hashlib.sha256,
                    "SHA384": hashlib.sha384,
                    "SHA512": hashlib.sha512}

                word = sha_funcs[type](word.encode()).hexdigest()

            # SHA3
            elif type in ("SHA3224", "SHA3256", "SHA3384", "SHA3512"):
                sha3_funcs = {
                "SHA3224": hashlib.sha3_224,
                "SHA3256": hashlib.sha3_256,
                "SHA3384": hashlib.sha3_384,
                "SHA3512": hashlib.sha3_512}

                word = sha3_funcs[type](word.encode()).hexdigest()

            # KECCAK
            elif type in ("KECCAK224", "KECCAK256", "KECCAK384", "KECCAK512"):
                k = keccak.new(digest_bits=int(type.replace("KECCAK", "")))
                k.update(word.encode())
                word = k.hexdigest()

            #shake
            elif type in ("SHAKE128", "SHAKE256"):
                shake_funcs = {
                    "SHAKE128": hashlib.shake_128,
                    "SHAKE256": hashlib.shake_256}

                digest_len = 64
                word = shake_funcs[type](word.encode()).hexdigest(digest_len)

            #pedmd
            elif type == "RIPEMD160":
                word = RIPEMD160.new(word).hexdigest()

            elif type == "PHPASS":
                word = phpass.hash(word)

            elif type == "BASE64" or type == "B64":
                word = base64.b64encode(word.encode("utf-8")).decode()

            else:
                if lang == "pt_BR":
                    print(invalidHash_ptBR(type))

                elif lang == "en_US":
                    print(invalidHash_en(type))

                else:
                    print(invalidHash_en(type))
                sys.exit(0)

        print(used)
        print(word)
