#!/usr/bin/python3
"""
Takes a URL and sends a request ti the url
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        urlreq = response.info()
        for key, value in urlreq.items():
            if key == "X-Request-Id":
                print(value)
