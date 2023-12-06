#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        three = i % 3
        five = i % 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        elif three == 0:
            print("Fizz", end=' ')
        elif five == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')
