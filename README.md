# zipkeygen
A simple Python CLI tool to securely generate and reproduce strong ZIP file passwords using PBKDF2-HMAC-SHA256 and salt. Great for consistent password-based encryption with ZIP tools like 7-Zip.


# zipkeygen

`zipkeygen` is a lightweight Python CLI tool for securely generating and recreating strong passwords for ZIP files. It uses the PBKDF2-HMAC-SHA256 algorithm with a unique random salt to derive consistent, secure passwords from a master password.

Ideal for ZIP file encryption tools like 7-Zip or WinRAR, this utility ensures that you can safely reproduce your ZIP password later — as long as you have your master password and saved salt.

---

## 🔐 Features

- Strong password generation using `PBKDF2-HMAC-SHA256`
- Automatically generates and prints a `salt` for reproducibility
- Recreate passwords anytime using the same master password + saved salt
- URL-safe base64 encoding (easy to copy into ZIP tools)
- Pure Python, cross-platform

---

## 🚀 Usage

### 1. Generate a new ZIP password
python zipkeygen.py
=== ZIP Password Generator ===
1. Generate new ZIP password
2. Recreate ZIP password from salt
Choose option (1/2): 1
Your master password (⚠️ visible input): myStrongMaster123

ZIP Password: NzlxSGdpMlEySklXQXN2Z2dKTW9vQXJ3U0t1Y2FiWmhjYlY
Salt (SAVE THIS): a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6

Save the salt somewhere safe — it's required to regenerate the same password later.


