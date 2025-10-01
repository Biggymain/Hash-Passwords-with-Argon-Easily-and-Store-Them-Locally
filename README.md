# 🔐 Hash Passwords with Argon2 — Store Securely on Your Local PC

**Goal:** securely convert plaintext or weakly-stored passwords into strong Argon2 hashes and keep those hashes stored *locally* on your machine. This repo helps you migrate or harden password storage by producing Argon2 hashed outputs (not by keeping plaintext long-term).

---

## 🚀 What this does (high-level)
- Reads user records that include plaintext passwords from `my_database.json`.
- Re-hashes each password using **Argon2** (via `argon2-cffi`) and adds an `argon2_hash` field to each user.
- Writes the resulting records to `argon2_users.json` stored locally on your PC.
- Intended to help you **remove plaintext** from storage and retain only strong hashes.

---

## ⚠️ Important security principle
The core aim is **local, safe storage of hashes** — *do not* keep plaintext files or push them to remote/public repos. After re-hashing, securely delete or encrypt the original plaintext file and restrict access to the generated hash file.

---

## 📂 Project structure
```

argon2-rehasher/
├─ cracked\_users.py        # Script that produces Argon2 hashes
├─ my\_database.json        # INPUT: plaintext passwords (keep this local, ephemeral)
├─ argon2\_users.json       # OUTPUT: Argon2 hashes (stored locally)
├─ requirements.txt
├─ README.md
├─ .gitignore
└─ LICENSE

````

---

## ⚙️ Installation
1. Clone the repo:
```bash
git clone https://github.com/Biggymain/Hash-Passwords-with-Argon-Easily-and-Store-Them-Locally.git
cd Hash-Passwords-with-Argon-Easily-and-Store-Them-Locally
````

2. (Recommended) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
# venv\Scripts\activate    # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

`requirements.txt` should contain:

```
argon2-cffi
```

---

## ▶️ Usage

1. Put your `my_database.json` (example format below) in the project folder:

```json
[
  {"username": "alice", "password": "mypassword123"},
  {"username": "bob", "password": "secretpass"}
]
```

2. Run the re-hash script:

```bash
python3 cracked_users.py
```

3. Result:

* `argon2_users.json` will be created/updated with an `argon2_hash` field for each user.
* Example output entry:

```json
{
  "username": "alice",
  "password": "mypassword123",
  "argon2_hash": "$argon2id$v=19$m=65536,t=3,p=4$..."
}
```

---

## 🔐 Suggested post-run steps (secure hygiene)

1. **Delete plaintext** immediately after verifying the hashes:

```bash
shred -u my_database.json   # or otherwise securely delete
```

2. **Restrict file permissions** for the hash file:

```bash
chmod 600 argon2_users.json
```

3. Keep the repo `.gitignore` configured so you never accidentally commit sensitive files:

```
my_database.json
argon2_users.json
.env
venv/
__pycache__/
```

4. Consider encrypting the `argon2_users.json` with a local key or using OS-level disk encryption for sensitive storage.

---

## ⚙️ Argon2 tuning (quick note)

* Argon2 parameters (memory, time, parallelism) can be tuned in `cracked_users.py` if needed. Higher memory/time increases resistance to cracking but costs CPU/RAM.
* The default `argon2-cffi` settings are secure for many use cases, but adjust for production-grade requirements.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## ⚖️ Disclaimer

This tool is for your own accounts and data only. Do **not** process accounts or passwords you do not own or have explicit permission to handle.

```
