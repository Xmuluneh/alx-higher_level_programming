#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = 0
digit = number % 10
digit = digit if number > 0 else -digit
if digit > 0:
    print("Last digit of {} is {} and is greater than 5".format(number, digit))
elif digit == 0:
    print("Last digit of {} is {} and is 0".format(number, digit))
elif digit < 0:
    print("Last digit of {} is {} and is less than 6 not 0".format(number, digit))
