import requests
import sys
import pyfiglet

ascii_banner = pyfiglet.figlet_format("DARKBYVED")
print(ascii_banner)

def check_onion_site(url):
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    try:
        print(f"[+] Checking: {url}")
        response = requests.get(url, proxies=proxies, timeout=10)
        print(f"    [Status]: {response.status_code}")
        print(f"    [Title]: {response.text.split('<title>')[1].split('</title>')[0] if '<title>' in response.text else 'N/A'}")
    except requests.exceptions.ConnectTimeout:
        print("    [!] Connection timed out.")
    except requests.exceptions.ConnectionError:
        print("    [!] Failed to connect. Is Tor running?")
    except Exception as e:
        print(f"    [!] Error: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 darkwebping.py <onion_url> [<onion_url2> ...]")
        sys.exit(1)

    for url in sys.argv[1:]:
        if not url.startswith("http"):
            url = "http://" + url
        check_onion_site(url)

if __name__ == "__main__":
    main()