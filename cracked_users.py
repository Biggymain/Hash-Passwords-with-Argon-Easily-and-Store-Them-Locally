import json
from argon2 import PasswordHasher

# Load your cracked users
with open("my_database.json", "r") as f:
    users = json.load(f)

# Initialize Argon2 hasher
ph = PasswordHasher()

# Re-hash passwords with Argon2
for user in users:
    plain_password = user["password"]
    user["argon2_hash"] = ph.hash(plain_password)

# Save new file with Argon2 hashes
with open("argon2_users.json", "w") as f:
    json.dump(users, f, indent=2)

print("Re-hashing complete. Saved to argon2_users.json")
