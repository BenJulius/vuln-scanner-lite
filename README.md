# Vulnerability Scanner Lite 🛡️

A lightweight, conceptual vulnerability scanner built in Python. This tool performs basic reconnaissance on a given URL to check for common misconfigurations and exposed services.

## Features

- **HTTPS Enforcement Check**: Verifies if the target automatically redirects to a secure HTTPS connection.
- **Security Header Analysis**: Inspects HTTP responses for crucial security headers (e.g., `Content-Security-Policy`, `X-Frame-Options`, `HSTS`).
- **Basic Port Scan**: Performs a fast TCP connect scan on common ports (21, 22, 80, 443, 3306, 8080) to identify exposed services.

## Prerequisites

- Python 3.x
- `requests` library

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone [https://github.com/BenJulius/vuln-scanner-lite.git](https://github.com/BenJulius/vuln-scanner-lite.git)
   cd vuln-scanner-lite
2. Install the required dependencies:

Bash
pip install -r requirements.txt

3. Run the scanner:

Bash
python scanner.py example.com

Disclaimer
This tool is for educational purposes only. Only scan domains and IP addresses that you own or have explicit permission to test.
