# main.py

import mymodule

# Greet the user
name = input("Enter your name: ")
mymodule.greet(name)

# Create Calculator object and perform calculations
calc = mymodule.Calculator()
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 - 4 = {calc.subtract(10, 4)}")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def display_student_info(self):
        self.display_info()
        print(f"Student ID: {self.student_id}")

# Take user input for Person and Student
try:
    person_name = input("Enter the person's name: ")
    person_age = int(input("Enter the person's age: "))
except ValueError:
    print("Invalid input for age. Age must be an integer.")
    person_age = None

if person_age is not None:
    person = Person(person_name, person_age)
    person.display_info()

try:
    student_name = input("Enter the student's name: ")
    student_age = int(input("Enter the student's age: "))
    student_id = input("Enter the student's ID: ")
    if not student_id:
        raise ValueError("Student ID cannot be empty.")
except ValueError as e:
    print(f"Error: {e}")
    student_age = None
    student_id = None

if student_age is not None and student_id is not None:
    student = Student(student_name, student_age, student_id)
    student.display_student_info()
