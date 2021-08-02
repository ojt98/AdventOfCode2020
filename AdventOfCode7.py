with open("Luggage") as opened_file:  # Reads in file and creates as list, each line is an element
    luggage = [line.rstrip("\n") for line in opened_file.readlines()]
dictionary = {}

def create_key_values_pairs_for_contained_bags():  # A function that creates key value pairs for the bags contained in
    # a bag.
    contained = [item.split(", ") for item in [item[item.index("contain") + 8:-1] for item in luggage]]  # For each bag,
    # creates a list that contains the bags it contains

    k = []  # Creates a list that contains lists with the names of each bag
    for bag in contained:
        placeholder = []
        for item in bag:
            placeholder.append(item[2:])
        k.append(placeholder)
    v = []  # Creates a list that contains lists with the count of bags
    for bag in contained:
        placeholder = []
        for item in bag:
            placeholder.append(item[0])
        v.append(placeholder)

    contained_bags = list((map(lambda x, y: dict(zip(x, y)), k, v)))
    return contained_bags  # Returns a list of key value pais. For each bag, a dictionary holds the bags it contains


def create_dictionary():  # Creates a dictionary structure. For each bag (key) it has as its value a dictioanry that
    # hold the other bags the key contains

    keys = [item[:item.index("contain") - 1] for item in luggage]
    counter = 0
    for key in keys:
        dictionary[key] = create_key_values_pairs_for_contained_bags()[counter]
        counter += 1
create_dictionary()

# once it has been searched need to removes from the dictionary!
layer = [key for key, value in dictionary.items() if "shiny gold bags" in value]
print(layer)
def drop_repetitive_keys(layer):
    for item in layer:
        del dictionary[item]



layer1 =[]
def tree(layer):
    for item in layer:
            layer1.append( [key for key, value in dictionary.items() if item in value])

tree(layer)

# for each element in the list apply a function






# def find_bags(first_layer):
#     for bag in first_layer:
#         bags.append([key for key, value in create_dictionary().items() if bag in value])
#     #find_bags(bags) # does the next layer
#
# find_bags(layer)
# for item in bags:
#     for bag in item:
#         find_bags(bag)
# print(bags)