import requests

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

try:
    response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=10)
    print("🕵️ Tor IP:", response.text)
except Exception as e:
    print("⚠️ Error:", e)
