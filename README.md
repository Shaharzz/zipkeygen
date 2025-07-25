# zipkeygen

`zipkeygen` is a lightweight Python CLI tool for securely generating and recreating strong passwords for ZIP files.  
It uses the PBKDF2-HMAC-SHA256 algorithm with a random salt to derive consistent, secure passwords from a master password.

This is perfect for tools like 7-Zip or WinRAR where you want strong, reproducible encryption without having to remember a long random password — just your master password and salt.

---

## 🔐 Features

- Strong password generation using PBKDF2-HMAC-SHA256  
- Unique random salt per password (16 bytes)  
- Recreate same password using saved salt and master password  
- Base64-encoded output for compatibility with ZIP tools  
- Pure Python, no external dependencies  
- Cross-platform and easy to use  

---

## 🚀 Usage

### 1. Generate a new ZIP password

```bash
python zipkeygen.py
```

```
=== ZIP Password Generator ===
1. Generate new ZIP password
2. Recreate ZIP password from salt
Choose option (1/2): 1
Your master password (⚠️ visible input): myStrongMaster123

ZIP Password: NzlxSGdpMlEySklXQXN2Z2dKTW9vQXJ3U0t1Y2FiWmhjYlY
Salt (SAVE THIS): a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6
```

Save the salt somewhere safe — it's required to regenerate the same password later.

---

### 2. Recreate a ZIP password from a saved salt

```bash
python zipkeygen.py
```

```
=== ZIP Password Generator ===
1. Generate new ZIP password
2. Recreate ZIP password from salt
Choose option (1/2): 2
Your master password (⚠️ visible input): myStrongMaster123
Saved salt: a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6

ZIP Password: NzlxSGdpMlEySklXQXN2Z2dKTW9vQXJ3U0t1Y2FiWmhjYlY
```

Same password is generated again — as long as your master password and salt match.

---

## 🧪 Technical Details

- **Algorithm**: PBKDF2-HMAC-SHA256  
- **Salt**: 16 random bytes, hex-encoded for storage  
- **Iterations**: 100,000 (can be adjusted in code)  
- **Derived key size**: 32 bytes  
- **Output format**: URL-safe Base64 (padding removed)  

---

## 📦 Requirements

- Python 3.6+

No external libraries are required. Uses only the Python standard library.

---

## ⚠️ Security Notice

- This tool uses `input()` instead of `getpass()` for compatibility with IDEs like **PyCharm**, which don’t support hidden input well.  
- If you're using it in a secure terminal environment (like a real shell), feel free to switch back to `getpass()` to hide input.  
- Your security depends on:
  - Choosing a strong **master password**
  - Storing the **salt** securely

---

## 📝 License

MIT License.  
Feel free to modify, improve, and share!

---

## 👨‍💻 Author

**Shahar David**

---

## 🔗 Related Tools

- [7-Zip](https://www.7-zip.org/) — Free, open-source file archiver with AES-256 encryption  
- [WinRAR](https://www.win-rar.com/) — Another ZIP/RAR archiver with encryption  
- [Python hashlib](https://docs.python.org/3/library/hashlib.html) — Official Python docs for PBKDF2 and other hash functions

---

## ⭐ Star this project

If you find this tool helpful, consider starring ⭐ the repository on GitHub!
