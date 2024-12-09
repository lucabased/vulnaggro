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
    
from shodan_utils import get_vuln
print(get_vuln("vuln:CVE-2024-23897", SHODAN_API_KEY))