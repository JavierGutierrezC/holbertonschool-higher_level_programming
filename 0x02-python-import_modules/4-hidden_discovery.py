#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)

    for x in range(len(names)):
        if not (names[x].startswith("__")):
            print(names[x])
