#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from assets import logo_ascii
print(logo_ascii)
# Load environment variables from .env file
load_dotenv()


# Retrieve the API key from environment variables
SHODAN_API_KEY = os.getenv('SHODAN_API_KEY')
if not SHODAN_API_KEY:
    print("[!] SHODAN_API_KEY is not set in the environment or .env file.")
    exit(1)
    
# Await input for CVE Code
import re
cve_code_input = ""
cve_regex = r'^CVE-\d{4}-\d{4,}$'
while not bool(re.match(cve_regex, cve_code_input)):
    cve_code_input = input("Input your CVE-Code: ").strip(" ")
print(f"\n[*] Searching for {cve_code_input}")

# CVE-2024-23897 
from shodan_utils import get_vuln
print(get_vuln(cve_code_input, SHODAN_API_KEY))