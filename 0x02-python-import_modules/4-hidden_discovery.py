#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    load = dir(hidden_4)
    for loads in load:
        if load[:2] != "__":
            print(loads)
