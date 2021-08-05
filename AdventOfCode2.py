pws = [str(x) for x in open("C:/Users/Oscar/OneDrive/Sparta Global/advent2.txt", "r")]
# count how many time letter occurs in pw


pw_list = [pws[i][pws[i].index(" ") + 4:] for i in range(len(pws))]
letter = [pws[i][pws[i].index(" ") + 1] for i in range(len(pws))]
limits = [(pws[i][:pws[i].index(" ")]) for i in range(len(pws))]
lower_lim = [limits[i][:limits[i].index("-")] for i in range(len(limits))]
upper_lim = [limits[i][limits[i].index("-") + 1:] for i in range(len(limits))]

valid_pws = 0
index = 0
for i in letter:
    if int(lower_lim[index]) <= pw_list[index].count(i) <= int(upper_lim[index]):
        valid_pws += 1
        index += 1
    else:
        index += 1
print(valid_pws)
