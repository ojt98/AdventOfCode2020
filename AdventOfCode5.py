boarding_passes = []
rows=[]
columns=[]


def open_file(file_name):     ## a function for opening file. Removes new line character and appends items into a list boarding_passes

    with open("BoardingPasses") as opened_file:
        for line in opened_file.readlines():
            boarding_passes.append(line.rstrip("\n"))

open_file("BoardingPasses")
print(boarding_passes)


class Boarding_check:       ##a class containing methods that impliment the logic for finding the upper and lower limits for letters B anf F

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound=lower_bound
        self.upper_bound=upper_bound

    def upper_half(self, type):         ##For letter B in a boarding pass we need to get the upper half of the range
                                        ##'columns' or 'rows' can be passed as arguments for 'type' parameter

        self.lower_bound=self.lower_bound+(((self.upper_bound+1)-self.lower_bound)/2)
        self.upper_bound=self.upper_bound
        if self.lower_bound==self.upper_bound:
            type.append(self.lower_bound)       ##if upper_bound and lower_bound converge on a B, we take this value as the row number



    def lower_half(self, type):         ##For letter F in a boarding pass we need to get the lower half of the range

        self.lower_bound = self.lower_bound
        self.upper_bound = self.lower_bound + ((self.upper_bound - (self.lower_bound + 1)) / 2)
        if self.lower_bound==self.upper_bound:
            type.append(self.lower_bound)       ##if upper_bound and lower_bound converge on an F, we take this value as the row number


class Rows(Boarding_check):     ##A class that contains a method for constructing a new list with the row numbers as elements

    def __init__(self, lower_bound, upper_bound):
        super().__init__(lower_bound, upper_bound)

    def find_rows(self):
        Obj = Rows(self.lower_bound, self.upper_bound)

        for index, boarding in enumerate(boarding_passes):
            for letter in boarding_passes[index]:

                if letter == "B":
                    Obj.upper_half(rows)
                elif letter == "F":
                    Obj.lower_half(rows)
                else:
                    Obj = Rows(self.lower_bound, self.upper_bound)
                    break

class Columns(Boarding_check):      ##A class that contains a method for constructing a new list with the column numbers as elements

    def __init__(self, lower_bound, upper_bound):
        super().__init__(lower_bound, upper_bound)

    def find_columns(self):
        Obj = Columns(self.lower_bound, self.upper_bound)

        for j in range(len(boarding_passes)):
            counter=0
            for letter in boarding_passes[j][7:10]:
                counter+=1
                if letter == "R":
                    Obj.upper_half(columns)

                if letter == "L":
                    Obj.lower_half(columns)
                if counter==3:
                    Obj = Columns(self.lower_bound, self.upper_bound)
                    break

row_lim=Rows(0,127)
row_lim.find_rows()

col_lim=Columns(0,7)
col_lim.find_columns()

print(rows)
print(columns)

result=list(map(lambda x,y:(x*8)+y,rows, columns))
print(max(result))
print(min(result))
