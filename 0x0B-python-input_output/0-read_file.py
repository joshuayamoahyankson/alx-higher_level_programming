def read_file(filename=""):
    with open(filename, "rt") as text_file:
        read_text = text_file.read()
        print(read_text)
    text_file.close()
    return read_text
