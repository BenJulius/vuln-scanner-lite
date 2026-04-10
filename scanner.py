import requests
import socket
import argparse
from urllib.parse import urlparse
import sys

# Common ports to scan
TARGET_PORTS = [21, 22, 23, 80, 443, 3306, 8080]

# Security headers to look for
SECURITY_HEADERS = [
    'Content-Security-Policy',
    'Strict-Transport-Security',
    'X-Content-Type-Options',
    'X-Frame-Options',
    'X-XSS-Protection'
]

def print_banner():
    print("-" * 50)
    print("🛡️  Vulnerability Scanner Lite")
    print("-" * 50)

def check_https(url):
    print("\n[+] Checking HTTPS Enforcement...")
    if not url.startswith("http"):
        url = "http://" + url
        
    try:
        response = requests.get(url, timeout=5)
        if response.url.startswith("https://"):
            print("  ✔️  HTTPS is enforced (Redirected successfully).")
        else:
            print("  ⚠️  HTTPS is NOT enforced. Data may be transmitted in plaintext.")
    except requests.exceptions.RequestException as e:
        print(f"  ❌ Error connecting to URL: {e}")

def check_headers(url):
    print("\n[+] Checking Security Headers...")
    if not url.startswith("http"):
        url = "http://" + url

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        
        for header in SECURITY_HEADERS:
            if header in headers:
                print(f"  ✔️  {header}: Found")
            else:
                print(f"  ⚠️  {header}: Missing")
    except requests.exceptions.RequestException:
        print("  ❌ Could not retrieve headers.")

def scan_ports(hostname):
    print(f"\n[+] Scanning Common Ports on {hostname}...")
    open_ports = []
    
    # Resolve hostname to IP
    try:
        target_ip = socket.gethostbyname(hostname)
        print(f"  Target IP: {target_ip}")
    except socket.gaierror:
        print("  ❌ Could not resolve hostname.")
        return

    for port in TARGET_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # 1 second timeout for faster scanning
        result = sock.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"  ⚠️  Port {port}: OPEN")
            open_ports.append(port)
        sock.close()

    if not open_ports:
        print("  ✔️  No common ports exposed.")

def main():
    parser = argparse.ArgumentParser(description="A lightweight vulnerability scanner.")
    parser.add_argument("url", help="The target URL to scan (e.g., example.com or https://example.com)")
    args = parser.parse_args()

    target_url = args.url
    
    # Extract hostname for port scanning
    parsed_url = urlparse(target_url)
    hostname = parsed_url.netloc if parsed_url.netloc else parsed_url.path

    print_banner()
    check_https(target_url)
    check_headers(target_url)
    scan_ports(hostname)
    print("\n[-] Scan Complete.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[-] Scan aborted by user.")
        sys.exit(0)
