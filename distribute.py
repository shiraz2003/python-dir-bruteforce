import requests
import argparse
import sys
from urllib.parse import urljoin

def parse_args():
    parser = argparse.ArgumentParser(
        description="Simple directory brute-force tool"
    )
    parser.add_argument(
        "--url", "-u",
        required=True,
        help="Base URL to scan (e.g., https://example.com/)"
    )
    parser.add_argument(
        "--wordlist", "-w",
        required=True,
        help="Path to wordlist file"
    )
    parser.add_argument(
        "--timeout", "-t",
        type=float,
        default=5.0,
        help="Request timeout in seconds (default: 5)"
    )
    parser.add_argument(
        "--status", "-s",
        type=int,
        nargs="*",
        default=[200],
        help="Show only these HTTP status codes (e.g., 200 301 403). Default: 200"
    )
    return parser.parse_args()

def load_wordlist(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except IOError as e:
        print(f"Error reading wordlist file: {e}")
        sys.exit(1)

