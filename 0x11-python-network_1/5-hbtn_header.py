#!/usr/bin/python3
"""
Takes a URL and sends a request ti the url
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    value = r.headers.get("X-Request-Id")
    print(value)
