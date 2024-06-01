import requests
from bs4 import BeautifulSoup
import re
import logging
import time

class Scanner:
    def __init__(self, url):
        self.url = url
        self.log_file = 'scan.log'
        self.log_setup()

    def log_setup(self):
        logging.basicConfig(filename=self.log_file, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def log_vulnerability(self, vuln_type, payload=None):
        logging.info(f"{vuln_type} vulnerability detected at {self.url} with payload {payload}")

    def scan_vulnerabilities(self):
        print("Starting vulnerability scan...")
        self.scan_sql_injection()
        self.scan_xss()
        self.scan_csrf()
        # Add more vulnerability scans here
        print("Vulnerability scan completed.")
        self.display_scan_results()

    def scan_sql_injection(self):
        # Simple SQL Injection test
        sql_payloads = ["' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' /*"]
        for payload in sql_payloads:
            response = requests.get(self.url, params={"id": payload})
            if "syntax" in response.text or "SQL" in response.text:
                self.log_vulnerability("SQL Injection", payload)
                print(f"SQL Injection vulnerability detected with payload: {payload}")

    def scan_xss(self):
        # Simple XSS test
        xss_payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"]
        for payload in xss_payloads:
            response = requests.get(self.url, params={"q": payload})
            if payload in response.text:
                self.log_vulnerability("XSS", payload)
                print(f"XSS vulnerability detected with payload: {payload}")

    def scan_csrf(self):
        # Simple CSRF test (placeholder)
        # This would be more complex in a real-world scenario
        pass

    def display_scan_results(self):
        # Display scan results with customized tool name and identifier
        print(f"Scan results displayed with customized tool name (<{{~{{ R,H }}~}}>) and identifier (📿☝️Muslim Army☝️📿)")

if __name__ == "__main__":
    url = input("Enter the URL to scan: ")
    if not url.startswith('http'):
        url = 'http://' + url

    scanner = Scanner(url)
    scanner.scan_vulnerabilities()
    
