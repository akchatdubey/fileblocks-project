#Implement a student class with information such as roll no,name and class the information must be entered by the user.
class Student:
    def __init__(self):
        self.rollno = input("Enter Roll Number: ")
        self.name = input("Enter Name: ")
        self.class_name = input("Enter Class Name: ")

    def __str__(self):
        return f"Roll No: {self.rollno}, Name: {self.name}, Class: {self.class_name}"

# Create a Student object and print its details
student = Student()
print(student)