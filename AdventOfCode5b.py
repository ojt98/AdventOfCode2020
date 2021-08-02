from AdventOfCode5 import *

for row in range(int(min(rows)), int((max(rows)))):
    for column in range(0, 7):
        id = (row * 8) + column
        if id not in result:
            if id + 1 and id - 1 in result:
                print(id)

##Notes

bookings = {}


def column_per_row(row_num):
    row_list = []
    for index, row in enumerate(rows):
        if row == row_num:
            row_list.append(columns[index])
    bookings[row_num] = row_list


for i in range(12, 122):
    column_per_row(i)
print(bookings)
