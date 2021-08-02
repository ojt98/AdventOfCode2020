import string

alphabet = list(string.ascii_lowercase)
CustomsQs = []


def open_file(file_name):  # a function for opening file. Removes new line character and appends items into a list
    # boarding_passes

    with open("CustomsQs") as opened_file:
        for line in opened_file.readlines():
            CustomsQs.append(line.rstrip("\n"))


open_file("CustomsQs")


def create_groups():
    groups = []
    group = ""

    for i in range(len(CustomsQs)):

        if CustomsQs[i] == "":
            groups.append(group)
            group = ""

            continue

        group += CustomsQs[i]

        if CustomsQs[i] == CustomsQs[-1]:
            groups.append(group)

    return (groups)


groups = create_groups()


def yes():
    counter = 0
    for f in range(len(groups)):
        for i in alphabet:
            if i in groups[f]:
                counter += 1
    print(counter)


yes()

