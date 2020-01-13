#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the body of the response
"""
import urllib.request
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    urlreq = argv[1]
    try:
        with urllib.request.urlopen(urlreq) as newurl:
            newurl = (newurl.read()).decode("utf-8")
            print(newurl)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
