'''
Task 2: Demonstrate List Slicing Problem Statement: Write a Python program that:
Creates a list of numbers from 1 to 10.
Extracts the first five elements from the list.
Reverses these extracted elements.
Prints both the extracted list and the reversed list
'''
# Code starts from here.
list1 = []
# Create the list of numbers from 1 to 10
for i in range(1,11):
    list1.append(i)
#Extract the first five elements from the list
list2 = list1[0:5]
# Reverse the extracted elements
reverse = list(reversed(list2))
# Prints both the extracted list and the reversed list
print("Original List : ", list1)
print("Extracted first five element :", list2)
print("Reversed extracted element :",reverse)
# Code ends here.
