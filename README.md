# 🧠 mshash - Multi-Stage Hashing Tool

**mshash** is a simple command-line tool written in Python for **encryption, brute-force attacks, and decryption** using multiple hash algorithms such as `SHA256`, `SHA512`, `MD5`, and Caesar cipher.

---

## 🔧 Features

- 🔐 Encrypt input strings using SHA256, SHA512, MD5, or Caesar cipher
- 🪓 Perform brute-force attacks on hashed values using a custom wordlist
- 🔓 Decrypt Caesar cipher by rotating through all possible shifts

---

## 🧰 Requirements

- Python 3.x
- Virtual environment (optional but recommended)
- A wordlist file for brute-force mode (e.g., `senhas.txt`)

---

## 💾 Installation

```bash
git clone https://github.com/yourusername/mshash.git
cd mshash
python3 -m venv venv
source venv/bin/activate
````

---

## 🚀 Usage

```bash
python3 mshash.py [-h] {e,b,d} {sha256,sha512,md5,caesar} [input] [wordlist] [hash_time]
```

### Arguments:

* `command`:

  * `e` = encrypt
  * `b` = brute-force
  * `d` = decrypt
* `hash_type`: `sha256`, `sha512`, `md5`, or `caesar`
* `input`: (optional) input string
* `wordlist`: file for brute-force mode
* `hash_time`: number of hash iterations (default = 1)

---

## 🔍 Examples

### Encrypt a string using SHA512

```bash
python3 mshash.py e sha512 123
```

### Brute-force a SHA512 hash using a wordlist

```bash
python3 mshash.py b sha512 <target_hash> senhas.txt 1
```

### Encrypt text using Caesar cipher

```bash
python3 mshash.py e caesar "hello world"
```

### Decrypt Caesar cipher

```bash
python3 mshash.py d caesar "khoor zruog"
```

---

## 📁 Project Structure

* `mshash.py`: Main command-line interface
* `cypher.py`: Contains the hashing and Caesar logic
* Wordlist file (e.g., `senhas.txt`): Used for brute-force attempts

---

## 🧑‍💻 License

This project is licensed under the **GNU General Public License v3.0**.

---

## 📬 Author

Made with ❤️ by \[Messias] on Debian
<br>
GitHub: [them3x/mshash](https://github.com/them3x/mshash)

