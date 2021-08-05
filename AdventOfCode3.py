tree_map = [str(x) for x in open("C:/Users/Oscar/OneDrive/Sparta Global/advent3.txt", "r")]

horr = 3
trees = 0

for i in range(1, (len(tree_map))):
    if horr >= 31:
        horr = horr % 31
    if tree_map[i][horr] == "#":
        horr += 3
        trees += 1
    else:
        horr += 3

print(trees)
