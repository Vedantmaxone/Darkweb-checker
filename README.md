⚙️ Requirements:

1. 🧱 Tor service running locally:

sudo apt install tor
sudo systemctl start tor


2. 📦 Python dependencies:

pip3 install requests[socks]


✅ Example Usage:

python3 Darkwebchecker.py http://3g2upl4pq6kufc4m.onion http://duskgytldkxiuqc6.onio
n

📦 Output Sample:

[+] Checking: http://3g2upl4pq6kufc4m.onion
    [Status]: 200
    [Title]: DuckDuckG
    o
    🛡️ Notes:

.onion domains are not DNS-resolvable — you must use a SOCKS5 proxy through Tor.

Some onion services require CAPTCHA or JS rendering — consider integrating selenium with Tor for those.
