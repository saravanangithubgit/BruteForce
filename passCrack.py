import itertools
import datetime

# 🔐 Interactive Password Combo Generator
print("🔐 Smart Password List Generator")

name = input("Enter full name (e.g., Hrithick Roshan): ").strip().lower()
username = input("Enter known username: ").strip().lower()
age = input("Enter age: ").strip()
dob = input("Enter date of birth (DDMMYYYY): ").strip()
pet = input("Enter pet name (optional): ").strip().lower()
extra_info = input("Do you know any other details? (e.g., favorite color, car, movie): ").strip().lower()
specials_choice = input("Include special characters? (yes/no): ").strip().lower()

# 🧠 Process inputs
name_parts = name.replace(".", "").replace(",", "").split()
dob_parts = [dob[i:i+2] for i in range(0, len(dob), 2)] if dob.isdigit() else []
extra_parts = extra_info.replace(",", "").split()

# 📦 Combine all words
words = set(name_parts + [username, pet, age, dob] + dob_parts + extra_parts)
words = {w for w in words if w}  # Remove empty entries

# Common suffixes and years
suffixes = ["123", "007", "786", "000", "999", "1234", "2024", "2025"]
years = [str(y) for y in range(1980, datetime.datetime.now().year + 1)]

# Special characters
specials = ["@", "#", "$", "_", ".", "!"] if specials_choice == "yes" else [""]

# 🔁 Generate combinations
combos = set()

# Single word + suffix + special
for word in words:
    for suf in suffixes + years:
        for sym in specials:
            combos.add(word + sym + suf)
            combos.add(suf + sym + word)

# Permutations of 2 words with/without symbol
for w1, w2 in itertools.permutations(words, 2):
    for sym in specials:
        combos.add(w1 + sym + w2)
        combos.add(w2 + sym + w1)

# Save to combo.txt
with open("combo.txt", "w") as f:
    for pwd in sorted(combos):
        f.write(pwd + "\n")

print(f"\n✅ combo.txt generated with {len(combos)} possible passwords.")
