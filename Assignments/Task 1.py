'''
Task 1: Calculate Factorial Using a Function
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
'''
# Code Starts from here..
# result= 1

def factorial(user_input):
    list1=list(range(1,user_input+1))
    result = 1
    for i in list1:
        result = result*i
    return result
    # print(list1)
    # return list1
user_input = int(input("Enter a number : "))
print(f"Factorial of {user_input} is :",factorial(user_input))

