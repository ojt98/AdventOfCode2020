def valid_passport(*fields):
    pp = [str(x) for x in open("C:/Users/Oscar/OneDrive/Sparta Global/advent4.txt", "r")]
    valid = 0
    counter = 0
    passport = 2
    for count, pp in enumerate(pp):
        if pp == "\n":  # at the end of a passport, when a new line occurs, counter is reset because we are searching
            # through a new passport
            counter = 0
            passport += 1
            continue
        # "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
        for j in range(len(fields)):
            if fields[j] in pp:  # for each element in the list checks if all the fields are in it and adds a
                # counter if it is valid
                location = pp.index(fields[j])
                if fields[j] == "byr":
                    if 1920 <= int(pp[location + 4:location + 8]) <= 2002:
                        counter += 1
                elif fields[j] == "iyr":
                    if 2010 <= int(pp[location + 4:location + 8]) <= 2020:
                        counter += 1
                elif fields[j] == "eyr":
                    if 2020 <= int(pp[location + 4:location + 8]) <= 2030:
                        counter += 1
                elif fields[j] == "hgt":
                    if "cm" in pp:
                        try:
                            if 150 <= int(pp[location + 4:pp.index("cm")]) <= 193:
                                counter += 1
                        except ValueError:
                            pass
                    elif "in" in pp:
                        try:
                            if 59 <= int(pp[location + 4:pp.index("in")]) <= 76:
                                counter += 1
                        except ValueError:
                            pass
                elif fields[j] == "hcl":
                    if pp[location + 4] == "#":
                        digit = 0
                        for x in pp[location + 5:location + 11]:
                            if x in ["a", "b", "c", "d", "e", "f"]:
                                digit += 1
                            elif x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                                digit += 1
                            if digit == 6:
                                counter += 1
                elif fields[j] == "ecl":
                    if pp[location + 4:location + 7] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        counter += 1
                elif fields[j] == "pid":
                    try:
                        ok = 0
                        if " " not in pp[location + 4:location + 13]:
                            for x in pp[location + 4:location + 13]:
                                if x.isdigit():
                                    ok += 1
                                if pp[location + 13].isdigit():
                                    break
                                if ok == 9:
                                    counter += 1
                    except IndexError:
                        pass
            else:  # if field is not in the element the element is skipped and we search the next element
                continue

        if counter == 7:  # if the counter is 7 (all fields are valid in the passport), valid is increased. And
            # counter is resist for the next passport
            valid += 1
            counter = 0
    return valid


print(valid_passport("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
