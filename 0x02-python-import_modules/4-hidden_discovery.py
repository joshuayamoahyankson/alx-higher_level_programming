#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    mod_names = dir(hidden_4)
    filter_names = [name for name in mod_names if not name.startswith("__")]
    filter_names.sort()

    for name in filter_names:
        print(name)
