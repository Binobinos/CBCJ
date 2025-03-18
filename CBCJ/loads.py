def load(file):
    lines = list(i.strip() for i in file.readlines())
    versions = lines[0].split(" ")[1][:-1]
    cry = False if lines[1].split("-")[1][:-1] == "F" else True
    print(versions)
    print(cry)
    if not cry:
        lines = lines[2:]
        if lines[0].startswith("dict"):
            data = dict()
        elif lines[0].startswith("list"):
            data = list()
        else:
            raise IndexError("Incorrect format")
        if type(data) == dict:
            print("".join(lines)[6:][:-2].split())

with open("example.CBCJ", "r") as file:
    a = load(file)