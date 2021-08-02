
map= [str(x) for x in open("C:/Users/Oscar/OneDrive/Sparta Global/advent3.txt", "r")]

def is_tree_at_coords(x_s,y):
    x= x_s%31
    return map[y][x]=="#"

def number_of_trees(x, y):
    x_coord=0
    y_coord=0
    trees=0
    while y_coord<len(map)-1:
        x_coord+=x
        y_coord+=y
        if is_tree_at_coords(x_coord, y_coord):
            trees+=1

    return(trees)

print(number_of_trees(1,1)*number_of_trees(5,1)*number_of_trees(7,1)*number_of_trees(1,2)*number_of_trees(3,1))

