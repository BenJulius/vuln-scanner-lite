# Vulnerability Scanner Lite 

A lightweight, conceptual vulnerability scanner built in Python. This tool performs automated reconnaissance to identify common web misconfigurations and exposed network services using native Python libraries.

![Vulnerability Scan Preview](scanner-preview.png)

## Infrastructure & Logic

This tool is designed for rapid security assessments, focusing on common entry points and configuration errors:

* **Analysis Engine:** Utilizes the `requests` library to audit HTTP response headers for security compliance.
* **Network Recon:** Implements a TCP connect scan via the `socket` module to verify port states on the target host.
* **CLI Orchestration:** Uses `argparse` for command-line argument handling and `urlparse` for target resolution.

## Features

* **HTTPS Enforcement Check:** Verifies if the target redirects to a secure connection to mitigate MITM risks.
* **Security Header Analysis:** Inspects responses for five crucial protections: CSP, HSTS, X-Content-Type-Options, X-Frame-Options, and X-XSS-Protection.
* **Port Scanning:** Probes common administrative and web ports (21, 22, 23, 80, 443, 3306, 8080) with built-in timeout handling.

## Skills Demonstrated

* **Application Security:** Practical knowledge of OWASP-related security headers and risk mitigation.
* **Network Engineering:** Understanding of TCP/IP handshakes, port states, and DNS resolution.
* **Python Automation:** Developing modular, reusable security tooling for auditing and reporting.

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/BenJulius/vuln-scanner-lite.git](https://github.com/BenJulius/vuln-scanner-lite.git)
   cd vuln-scanner-lite
   
2. Install dependencies:

Bash
pip install requests
3. Run the scanner:

Bash
python scanner.py benjulius.dev
## Disclaimer
This tool is for educational purposes only. Only scan domains and IP addresses that you own or have explicit permission to test.
