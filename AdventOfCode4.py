pp = [str(x) for x in open("C:/Users/Oscar/OneDrive/Sparta Global/advent4.txt", "r")]

data = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = 0
counter = 0
for index, pp in enumerate(pp):
    print(pp)
    if pp == "\n":
        counter = 0
        continue
    for j in range(len(data)):
        if data[j] in pp:
            counter += 1
    if counter == 7:
        valid += 1
        counter = 0
print(valid)
