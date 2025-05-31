'''
Task 1: Create a Dictionary of Student Marks
Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''
# Code starts from here..
result = {"Sawan":95,"Harsh":80}
name=input("Enter the student's name :")
if (name in result):
   value = result.get(name)
   print(f"{name}'s marks :{value}")
else:
    print("Student not found.")
# Code ends here.


