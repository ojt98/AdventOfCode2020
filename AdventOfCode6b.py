from AdventOfCode6 import *

new = []
for i in range(len(CustomsQs)):
    if CustomsQs[i] == "":
        new.append(i)

# #using all the letters in the first item in the first item of each grroup, search if they exists in the remaining items

new1 = list(map(lambda x: x + 1, new))
new = new[1:]


def total():
    groups = []
    groups.append([a for a in CustomsQs[0:5]])
    for x in range(len(new)):
        groups.append([a for a in CustomsQs[new1[x]:new[x]]])
    groups.append([a for a in CustomsQs[-3:]])

    counter = 1
    result = 0

    for s in range(len(groups)):

        if len(groups[s]) == 1:  # accounting for groups with only 1 entry
            result += len(groups[s][0])

        for j in set(groups[s][0]):
            for x in range(1, len(groups[s])):
                print(groups[s])
                if j not in groups[s][x]:
                    counter = 1
                    break
                if j in groups[s][x]:
                    counter += 1
                    print(counter)
                    if counter == len(groups[s]):
                        result += 1
                        print(result)
                        counter = 1
    print(result)


total()
# intersection of groups
