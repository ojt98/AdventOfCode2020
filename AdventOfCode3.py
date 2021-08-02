
map= [str(x) for x in open("C:/Users/Oscar/OneDrive/Sparta Global/advent3.txt", "r")]


horr=3
trees=0

for i in range(1,(len(map))):

    if horr>=31:
        horr=horr%31
        print("b")
        print(horr)

    if map[i][horr]=="#":

        horr += 3
        trees+=1
        print("a")
        print(horr)

    else:
        horr+=3

print(trees)





# def is_tree_at_coordinates(hill_x, hill_y):
#     map_x = hill_x % 31
#     return map[hill_y][map_x] == "#"
# def tree_count_for_slope(right_increment, down_increment):
#     right_coordinate = 0
#     down_coordinate = 0
#     tree_count = 0
#
#     while down_coordinate < len(map):
#         if is_tree_at_coordinates(right_coordinate, down_coordinate):
#             tree_count += 1
#         right_coordinate += right_increment
#         down_coordinate += down_increment
#
#     return tree_count

# print(tree_count_for_slope(3,1))