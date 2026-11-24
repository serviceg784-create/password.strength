<div align="center">

# 🔐 Password Hashing Lab

### A simple Python program that hashes passwords and verifies them using a salt

**Python 3.8+** | **PBKDF2-HMAC-SHA256** | **No external dependencies** | **Educational project**

</div>


---

## ✨ Features

| Feature | Description |
|---|---|
| 🧬 **PBKDF2-HMAC-SHA256** | Derives a password hash using a password-based key derivation function |
| 🧂 **Unique salt** | Generates a fresh, cryptographically random 16-byte salt for each hash |
| 🔁 **Password verification** | Checks a re-entered password against the original hash |
| 🛡️ **Constant-time comparison** | Uses `hmac.compare_digest` for hash comparison |
| 🪶 **Lightweight** | Runs with Python's standard library; no third-party packages |
| 🧪 **No disk storage** | Keeps this demo's password, salt, and hash in memory only |

---

## 🧰 Tech Stack

| Technology | Role |
|:---:|---|
| 🐍 **Python** | Core programming language |
| `hashlib` | PBKDF2-HMAC-SHA256 derivation |
| `secrets` | Cryptographically secure salt generation |
| `hmac` | Constant-time comparison utility |

---

## ⚙️ Run it

**Requirements:** Python 3.8 or newer

```bash
git clone <your-repository-url>
cd <your-repository-folder>
python3 main.py
```

> Replace the clone URL and folder name with your own repository details after you upload this project.

---

## 🔍 How it works

```text
       ┌───────────────────┐
       │  Enter password  │
       └─────────┬─────────┘
                 ▼
       ┌───────────────────┐
       │ Generate random  │
       │      salt        │
       └─────────┬─────────┘
                 ▼
       ┌───────────────────┐
       │ PBKDF2 derives   │
       │ password hash   │
       └─────────┬─────────┘
                 ▼
       ┌───────────────────┐
       │ Show salt + hash │
       └─────────┬─────────┘
                 ▼
       ┌───────────────────┐
       │ Re-enter password│
       └─────────┬─────────┘
                 ▼
       ┌───────────────────┐
       │ Constant-time    │
       │ verification    │
       └─────────┬─────────┘
                 ▼
       ┌────────────────────────┐
       │ ✅ Match / ❌ No match │
       └────────────────────────┘
```

### 🔬 Parameters

| Parameter | Value |
|---|---:|
| Hash algorithm | SHA-256 |
| Iterations | 600,000 |
| Salt size | 16 bytes |
| Derived hash size | 32 bytes |

---

## ▶️ Sample session

```text
================================================
       PASSWORD HASHING DEMONSTRATION
================================================
Enter a password to hash: ********

Generated result
Algorithm : PBKDF2-HMAC-SHA256 (600,000 iterations)
Salt     : <random salt value>
Hash     : <derived hash value>

Verify a password
Enter password again: ********
Result   : Password matches.
```

*The salt and hash shown in a real run will be different each time.*

---

## 📚 Learning note

🔒 **Hashing is one-way.** It is designed to verify a password, not recover the original password from the hash.

This is an educational CLI demo: it does not save credentials to disk. It illustrates the hashing and verification flow, not a complete production authentication system.

---

<div align="center">

### Made for learning 🧑‍💻

*Understand the process. Don't just run the code.*

</div>
