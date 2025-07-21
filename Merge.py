
combo_file = "combo.txt"
rockyou_file = "rockyou.txt"
output_file = "merged_wordlist.txt"

passwords = set()

with open(combo_file, "r", encoding="utf-8", errors="ignore") as f1:
    for line in f1:
        passwords.add(line.strip())

with open(rockyou_file, "r", encoding="utf-8", errors="ignore") as f2:
    for line in f2:
        passwords.add(line.strip())

with open(output_file, "w", encoding="utf-8") as out:
    for pwd in sorted(passwords):
        out.write(pwd + "\n")

print(f"✅ Merged {len(passwords)} unique passwords into '{output_file}'")
