import random


def add_numbers(*args):
    total = 0
    for value in args:
        total += value
        print("current value: ", value)
    print(total)

x = random.randrange(1, 90)
print(x)
