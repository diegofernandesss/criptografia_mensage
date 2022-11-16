def open_txt(file):
    with open(file) as f:
        return "".join(f.read())