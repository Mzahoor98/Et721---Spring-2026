"""
Muhammad Zahoor
Feb 5, 2026
Lab 5, functions
"""
import math
from lab5_function_zahoor import *

print('\n----- Example 1: user-defined function')
w = 10
length = 2
a = area_rectangle(w,length)
print_area_result(w,length,a)

print('\n----- Example 2: calculate')
x1 = collectnum()
x2 = collectnum()
y1 = collectnum()
y2 = collectnum()

# Testing
print(f"({x1},{y1})({x2},{y2})")

# testing 
print(f"distance = {calculate_distance(x1,x2,y1,y2)}")

distance = calculate_distance(x1,x2,y1,y2)
print_distance(x1,x2,y1,y2,distance)

print('\nEXERCISE')
import random

GUESS_NUMBER = 5

def generate_random_number(min_num, max_num):
    return random.randint(min_num, max_num)

def compare_numbers(random_number):
    if random_number < GUESS_NUMBER:
        print("The number is smaller than the guess number")
    elif random_number > GUESS_NUMBER:
        print("The number is bigger than the guess number")
    else:
        print("You got it!")

random_num = generate_random_number(1, 9)
compare_numbers(random_num)
