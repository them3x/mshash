# 🧠 mshash - Multi-Stage Hashing Tool

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-AGPL-green)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Unix-lightgrey)

> A command-line tool for multi-stage hashing and encoding. Supports classic hashes, modern SHA-3, Keccak, Base64, and even PHPass (WordPress-style).

---

## 🚀 Features

- 🔐 Classic hash algorithms: MD2, MD4, MD5
- 🔐 SHA-2 & SHA-3 families
- 🔐 Keccak variants
- 🔁 Base64 encoding
- 🧩 PHPass (WordPress password hashing)
- 🗣️ Multilingual help (Português 🇧🇷 & English 🇺🇸)
- 🧪 Apply multiple stages of hashing (e.g., `base64(sha512(md5(text)))`)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/them3x/mshash.git
cd mshash
````

Install dependencies:

```bash
pip install -r requirements.txt
```

> 📦 Requires: `pycryptodome`, `passlib`, `distro` (optional)

---

## 🧑‍💻 Usage

```bash
python3 mshash.py [ALGORITHMS...] -t"TEXT"
```

Or interactively:

```bash
python3 mshash.py [ALGORITHMS...]
```

---

## 💡 Examples

```bash
# SHA512 hash of "123"
python3 mshash.py sha512 -t"123"

# Multi-stage: base64(sha512(md5("hello")))
python3 mshash.py md5 sha512 base64 -t"hello"

# Interactive input
python3 mshash.py md5 sha256
Type:
```

---

## 🔤 Supported Algorithms

### 🔸 Classic Hashes

* `MD2`, `MD4`, `MD5`

### 🔹 SHA-2

* `SHA224`, `SHA256`, `SHA384`, `SHA512`

### 🔹 SHA-3

* `SHA3224`, `SHA3256`, `SHA3384`, `SHA3512`

### 🔹 Keccak

* `KECCAK224`, `KECCAK256`, `KECCAK384`, `KECCAK512`

### 🔸 Others

* `RIPEMD160`
* `PHPASS` (WordPress hashing)

### 🔁 Encodings

* `BASE64`, `B64`

---

## 🌐 Language Detection

* The tool detects your system language using `locale`.
* Displays help messages in:

  * 🇧🇷 **Português (pt\_BR)**
  * 🇺🇸 **English (en\_US or others)**

---

## 🧾 License

GNU LESSER GENERAL PUBLIC LICENSE

---

## 👤 Author

Made with ❤️ by \[Messias] on Debian
<br>
GitHub: [them3x/mshash](https://github.com/them3x/mshash)


---

## ❤️ Contributions

Pull requests and feature suggestions are welcome!
