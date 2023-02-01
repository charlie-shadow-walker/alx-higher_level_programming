#!/usr/bin/python3

number = 0
for i in range(0, 100):
    if i < 10:
        number = "0" + f"{i}"
    else:
        number = i
    if i < 99:
        print("{}, ".format(number), end="")
    else:
        print("{}".format(number))
