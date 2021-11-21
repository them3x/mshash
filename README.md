# mshash
PyCode for encode/decode (MD5, SHA256, Base64, cipher caesar, overutf8)

------

> Dependecies
- python 2.7
- hashlib (PyLIB)
- sys (PyLIB
- os (PyLIB)


---------

#### Usage

- Decoding base64
> python2 mshash.py -d <base64/b64> aGk=
- Encoding Base64
> python2 mshash.py -e <base64/b64> hello

- Decoding hash (md5/sha256)
>python2 mshash.py -d \<md5/sha256> \<hash> <wordlist file\>
  
- Encoding hash (md5/sha256)
>python2 mshash.py -e \<md5/sha256> <hash\>

- More Usage
> python2 mshash.py --help
