pws = [str(x) for x in open("C:/Users/Oscar/OneDrive/Sparta Global/advent2.txt", "r")]

limit = []
upper = []
lower = []
invalid = []
count = 0

for i in pws:
    limit = i.split(": ")[0]
    pw = i.split(": ")[1]
    character = limit.split(" ")[1]
    spread = limit.split(" ")[0]
    upper_limit = spread.split("-")[1]
    lower_limit = spread.split("-")[0]

    if character == pw[int(lower_limit) - 1]:
        if character != pw[int(upper_limit) - 1]:
            count += 1
    if character != pw[int(lower_limit) - 1]:
        if character == pw[int(upper_limit) - 1]:
            count += 1

print(count)
