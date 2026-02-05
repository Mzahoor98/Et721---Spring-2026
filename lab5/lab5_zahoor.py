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
y1 = collect()
y2 = collectnum()

# Testing
print(f"({x1},{y1})({x2},{y2})")

# testing 
print(f"distance = {calculate_distance(x1,x2,y1,y2)}")

distance = calculate_distance(x1,x2,y1,y2)
print_distance(x1,x2,y1,y2,distance)

print('\nEXERCISE')