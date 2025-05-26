'''
Task 2: Using the Math Module for Calculations
 Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
'''
# Code start from here
import math #import math module
user_input = int(input("Enter a number : ")) # Ask the user for a number as input
square_root = math.sqrt(user_input) # Calculate Square root of the number
log = math.log(user_input) # Calculate Natural logarithm (log base e) of the number
sine = math.sin(user_input) # Calculate Sine of the number (in radians)
# Displays the calculated results.
print("Square root :", square_root)
print("Logarithm :", log)
print("Sine :", sine)
#Code end here

