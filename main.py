#encoding: UTF-8
import getpass
import sys
from lang import help_ptBR, help_en
from cypher import Cypher
import locale

locale.setlocale(locale.LC_ALL, '')
lang, cod = locale.getlocale()


v = "v2.0.0"
if len(sys.argv) == 1:
    if lang == "pt_BR":
        print(help_ptBR(v))
    elif lang == "en_US":
        print(help_en(v))
    else:
        print(help_en(v))

    sys.exit(0)

# Permite especificação do texto direto via argumento
# -w"Word to hashing"
if len(sys.argv[-1:][0]) > 2 and sys.argv[-1:][0][:2] == "-t":
    word = sys.argv[-1:][0][2:]
    hashs = sys.argv[1:][:-1]

# Permite uso de getpass para digitar o texto
else:
    hashs = sys.argv[1:]
    word = getpass.getpass("Type: ")

Cypher.hashs(hashs, word, lang)

