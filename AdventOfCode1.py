lines= [int(x) for x in open("C:/Users/Oscar/OneDrive/Sparta Global/advent1.txt", "r")]



for a in lines:
    for b in lines:
        if a+b == 2020:
            print(f" {a}+{b} =2020 \n {a}*{b}={a*b}")

