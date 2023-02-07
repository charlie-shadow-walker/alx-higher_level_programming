#!/usr/bin/python3

def fizzbuzz():
    element = ""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            element = "FizzBuzz"
        elif i % 3 == 0:
            element = "Fizz"
        elif i % 5 == 0:
            element = "Buzz"
        else:
            element = f"{i}"

        if i < 100:
            print("{} ".format(element), end="")
        else:
            print("{} ".format(element), end="")
