
# ENGLISH
def help_en(v):
    return f"""╔════════════════════════════════════════════════════════════╗
║          mshash - Multi-stage Hashing Tool {v}          ║
╚════════════════════════════════════════════════════════════╝

Usage:
  python3 mshash.py [ALGORITHMS...] -t"TEXT"
  python3 mshash.py [ALGORITHMS...]  (enter text interactively)

Examples:
  ~$ python3 mshash.py sha512 -t"123"
  ~$ python3 mshash.py base64 sha512 md5
  ~$ python3 mshash.py md5 sha256

Supported Algorithms:

  Classic Hashes:
   MD2
   MD4
   MD5

  SHA-2:
   SHA224
   SHA256
   SHA384
   SHA512

  SHA-3:
   SHA3224
   SHA3256
   SHA3384
   SHA3512

  Keccak:
   KECCAK224
   KECCAK256
   KECCAK384
   KECCAK512

  Others:
   RIPEMD160
   PHPASS (WordPress)

  Encodings:
   BASE64 / B64

Notes:
  - Algorithms are applied in reverse order (last one is applied first).
    Example: base64(sha512(md5(text)))

  - Use `-t` to pass text directly via command line.
    Without `-t`, the program will ask for input securely.

Author:
  4D3358 - https://github.com/them3x/mshash
"""

def invalidHash_en(hash_name):
    return f"[!] The hash {hash_name} is not implemented :("


# PORTUGUES BR
def help_ptBR(v):
    return f"""╔════════════════════════════════════════════════════════════╗
║          mshash - Multi-stage Hashing Tool {v}          ║
╚════════════════════════════════════════════════════════════╝

Uso:
  python3 mshash.py [ALGORITMOS...] -t"TEXTO"
  python3 mshash.py [ALGORITMOS...] (digite o texto interativamente)

Exemplos:
  ~$ python3 mshash.py sha512 -t"123"
  ~$ python3 mshash.py base64 sha512 md5
  ~$ python3 mshash.py md5 sha256

Algoritmos Suportados:

  Hashes clássicos:
   MD2
   MD4
   MD5

  SHA-2:
   SHA224
   SHA256
   SHA384
   SHA512

  SHA-3:
   SHA3224
   SHA3256
   SHA3384
   SHA3512

  Keccak:
   KECCAK224
   KECCAK256
   KECCAK384
   KECCAK512

  Outros:
   RIPEMD160
   PHPASS (WordPress)

  Codificações:
   BASE64 / B64

Notas:
  - Os algoritmos são aplicados em ordem reversa (último primeiro).
    Exemplo: base64(sha512(md5(texto)))

  - Use `-t` para especificar o texto direto na linha de comando.
    Sem `-t`, o programa pedirá a entrada de forma segura.

Autor:
  4D3358 - https://github.com/them3x/mshash

"""

def invalidHash_ptBR(hash_name):
    return f"[!] A hash {hash_name} não esta implementada :("

