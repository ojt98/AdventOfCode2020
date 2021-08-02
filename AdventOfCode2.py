pws= [str(x) for x in open("C:/Users/Oscar/OneDrive/Sparta Global/advent2.txt", "r")]
#count how many time letter occurs in pw

print(pws)


pw_list=[]
for i in range(len(pws)):

    pw_list.append(pws[i][pws[i].index(" ")+4:]) ##can use plit() which creates a list with elements that are seperated by the input example pws[0].split("-")[0]
                                                ##splits the first element using - and creates a list when the elements eithe side.
print(pw_list)
letter=[]
for i in range(len(pws)):

    letter.append((pws[i][pws[i].index(" ")+1]))
print(letter)
limits=[]
for i in range(len(pws)):

    limits.append(((pws[i][:pws[i].index(" ")])))
print(limits)

lower_lim=[]
for i in range(len(limits)):
    lower_lim.append(limits[i][:limits[i].index("-")])
print(lower_lim)

upper_lim=[]
for i in range(len(limits)):
    upper_lim.append(limits[i][limits[i].index("-")+1:])
print(upper_lim)

valid_pws = 0
index = 0
for i in letter:

    if pw_list[index].count(i)>=int(lower_lim[index]) and pw_list[index].count(i)<=int(upper_lim[index]):
        valid_pws+=1
        index+=1
    else:
        index+=1
print(valid_pws)

##Refactoring

# invalid_passwords = []
# valid_passwords = []
#
# for i in list:
#     policy = (i.split(": ")[0])
#     password1 = (i.split(": ")[1])
#     password = password1.splitlines()[0] ##using splitlines to remove the white space at the end of the line
#     policy_range = policy.split(" ")[0]
#     policy_character = policy.split(" ")[1]
#     range_lower = int(policy_range.split("-")[0])
#     range_upper = int(policy_range.split("-")[1])
#     count = password.count(policy_character)
#
#     if count not in range(range_lower, range_upper + 1):
#         invalid_passwords.append(i)
#     else:
#         valid_passwords.append(i)
#
# print(len(valid_passwords))





