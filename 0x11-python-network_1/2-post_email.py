#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed URL
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    mail = {"email": argv[2]}
    data = urllib.parse.urlencode(mail)
    data = data.encode("utf-8")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        urlreq = response.read()
        print(urlreq.decode("UTF-8"))
