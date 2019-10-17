#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    file_9 = load_from_json_file("add_item.json")
except:
    file_9 = []

filename = "add_item.json"
for argc in range(1, len(sys.argv)):
    file_9.append(sys.argv[argc])
save_to_json_file(file_9, filename)
