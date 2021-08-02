pp= [str(x) for x in open("C:/Users/Oscar/OneDrive/Sparta Global/advent4.txt", "r")]
print(pp)


# valid=0
# counter=0
# for i in range(len(pp)):
#
#     if pp[i]=="\n":
#         counter = 0
#         continue
#     for j in range(len(data)):
#         if data[j] in pp[i]:
#             counter+=1
#     if counter==7:
#         valid+=1
#         counter=0
# print(valid)


pp= [str(x) for x in open("C:/Users/Oscar/OneDrive/Sparta Global/advent4.txt", "r")]
print(pp)
data=[ "byr","iyr","eyr","hgt","hcl","ecl","pid"]
valid=0
counter=0
for index, pp in enumerate(pp): #iterating over each element in the list
    print(pp)
    if pp=="\n":                #resets counter for a new passpord
        counter=0
        continue
    for x, data in enumerate(data):  ## after the first full loop data=pid (the last entry of data)
                                    ##then after the second full loop data=d, the last element of data^
        print(data)
        if data in pp:
            counter+=1
            print(counter)

    if counter==7:              #if a passport has 7 types its valid!
        valid+=1
        counter=0
print(valid)


# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (country ID)

data=[ "byr","iyr","eyr","hgt","hcl","ecl","pid"]
valid=0
counter=0
for index, pp in enumerate(pp):
    print(pp)
    if pp=="\n":

        counter=0
        continue
    for j in range(len(data)):
        if data[j] in pp:
            counter+=1
    if counter==7:
         valid+=1
         counter=0
print(valid)
