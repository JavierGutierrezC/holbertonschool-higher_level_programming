#!/usr/bin/python3

import json

def load_from_json_file(filename):
    with open(filename, "r", encoding="UTF-8") as file_8:
        return (json.load(file_8))
