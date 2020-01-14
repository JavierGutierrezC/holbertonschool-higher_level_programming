#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request with letter as parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) is 1 or not argv[1].isalpha():
        # print(len(argv))
        # print(argv[0])
        # print(argv[2])
        print("No result")
    else:
        url = "http://0.0.0.0:5000/search_user"
        q = argv[1]
        r = requests.post(url, data={"q": q})
        # print(r.text)
        # print(r.json())
        jason = r.json()
        try:
            print("[{}] {}".format(jason.get("id"), jason.get("name")))
        except ValueError:
            print("Not a valid JSON")
