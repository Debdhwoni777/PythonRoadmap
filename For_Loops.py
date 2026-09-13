# ============================================================
#                ADVANCED FOR LOOPS IN PYTHON
# ============================================================
#
# Topics:
# 1. Iterating over complex data
# 2. enumerate()
# 3. zip()
# 4. Nested loops
# 5. for + else
# 6. Conditional iteration
# 7. Dictionary iteration
# 8. Unpacking
# 9. range() with different steps
# 10. break
# 11. continue
# 12. Comprehensions
# 13. Practical mini challenges
#
# ============================================================


# ------------------------------------------------------------
# 1. ITERATING OVER A LIST
# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# ------------------------------------------------------------
# 2. ENUMERATE()
# ------------------------------------------------------------
#
# enumerate() gives:
# index + value
#
# ------------------------------------------------------------

subjects = ["Mathematics", "Bangla", "English", "History", "Geography"]

for index, subject in enumerate(subjects):
    print(index, subject)


# Start indexing from 1

for index, subject in enumerate(subjects, start=1):
    print(index, subject)


# ------------------------------------------------------------
# 3. ZIP()
# ------------------------------------------------------------
#
# zip() combines multiple iterables.
#
# ------------------------------------------------------------

students = ["Dhwoni", "Rahul", "Arjun", "Riya"]

marks = [95, 87, 76, 91]

for student, mark in zip(students, marks):
    print(student, ":", mark)


# ------------------------------------------------------------
# 4. ZIP() WITH MULTIPLE LISTS
# ------------------------------------------------------------

names = ["Dhwoni", "Rahul", "Arjun"]

ages = [15, 16, 15]

grades = ["A+", "A", "B"]

for name, age, grade in zip(names, ages, grades):
    print(name, age, grade)


# ------------------------------------------------------------
# 5. UNPACKING INSIDE A FOR LOOP
# ------------------------------------------------------------

students = [
    ("Dhwoni", 95),
    ("Rahul", 87),
    ("Arjun", 76)
]

for name, marks in students:
    print(name, marks)


# ------------------------------------------------------------
# 6. DICTIONARY ITERATION
# ------------------------------------------------------------

student = {
    "name": "Dhwoni",
    "age": 15,
    "grade": "A+",
    "average": 92.5
}

for key in student:
    print(key)


# Keys and values

for key, value in student.items():
    print(key, ":", value)


# Only values

for value in student.values():
    print(value)


# Only keys

for key in student.keys():
    print(key)


# ------------------------------------------------------------
# 7. NESTED FOR LOOPS
# ------------------------------------------------------------

for row in range(1, 4):

    for column in range(1, 4):
        print(row, column)


# ------------------------------------------------------------
# 8. MULTIPLICATION TABLE
# ------------------------------------------------------------

number = 7

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# ------------------------------------------------------------
# 9. RANGE() WITH STEP
# ------------------------------------------------------------

for number in range(0, 21, 2):
    print(number)


# Reverse order

for number in range(20, 0, -2):
    print(number)


# ------------------------------------------------------------
# 10. FOR LOOP + CONDITION
# ------------------------------------------------------------

numbers = [12, 5, 18, 7, 25, 3, 40]

for number in numbers:

    if number >= 20:
        print(number)


# ------------------------------------------------------------
# 11. CONTINUE
# ------------------------------------------------------------
#
# continue skips the current iteration.
#
# ------------------------------------------------------------

for number in range(1, 11):

    if number % 2 == 0:
        continue

    print(number)


# ------------------------------------------------------------
# 12. BREAK
# ------------------------------------------------------------
#
# break completely stops the loop.
#
# ------------------------------------------------------------

for number in range(1, 11):

    if number == 6:
        break

    print(number)


# ------------------------------------------------------------
# 13. FOR + ELSE
# ------------------------------------------------------------
#
# The else block runs when the loop finishes normally.
# It does NOT run if the loop is stopped by break.
#
# ------------------------------------------------------------

numbers = [2, 4, 6, 8, 10]

for number in numbers:

    if number % 2 != 0:
        print("Odd number found")
        break

else:
    print("All numbers are even")


# ------------------------------------------------------------
# 14. SEARCHING USING FOR + ELSE
# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

search = 30

for number in numbers:

    if number == search:
        print("Number found:", number)
        break

else:
    print("Number not found")


# ------------------------------------------------------------
# 15. NESTED DATA
# ------------------------------------------------------------

students = [
    {
        "name": "Dhwoni",
        "marks": [95, 88, 92]
    },
    {
        "name": "Rahul",
        "marks": [78, 85, 80]
    },
    {
        "name": "Arjun",
        "marks": [65, 72, 69]
    }
]

for student in students:

    print("Student:", student["name"])

    for mark in student["marks"]:
        print("Mark:", mark)


# ------------------------------------------------------------
# 16. CALCULATE TOTALS
# ------------------------------------------------------------

marks = [85, 92, 78, 95, 88]

total = 0

for mark in marks:
    total += mark

print("Total:", total)


# ------------------------------------------------------------
# 17. FIND MAXIMUM WITHOUT max()
# ------------------------------------------------------------

numbers = [45, 12, 89, 34, 67, 91, 23]

highest = numbers[0]

for number in numbers:

    if number > highest:
        highest = number

print("Highest:", highest)


# ------------------------------------------------------------
# 18. FIND MINIMUM WITHOUT min()
# ------------------------------------------------------------

lowest = numbers[0]

for number in numbers:

    if number < lowest:
        lowest = number

print("Lowest:", lowest)


# ------------------------------------------------------------
# 19. COUNTING WITH A LOOP
# ------------------------------------------------------------

numbers = [10, 15, 20, 25, 30, 35, 40]

count = 0

for number in numbers:

    if number > 20:
        count += 1

print("Numbers greater than 20:", count)


# ------------------------------------------------------------
# 20. STRING ITERATION
# ------------------------------------------------------------

word = "Python"

for character in word:
    print(character)


# ------------------------------------------------------------
# 21. COUNT CHARACTERS
# ------------------------------------------------------------

text = "Python Programming"

vowels = 0

for character in text.lower():

    if character in "aeiou":
        vowels += 1

print("Vowels:", vowels)


# ------------------------------------------------------------
# 22. NESTED LOOP — MATRIX
# ------------------------------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:

    for value in row:
        print(value, end=" ")

    print()


# ------------------------------------------------------------
# 23. DICTIONARY + NESTED DATA
# ------------------------------------------------------------

school = {
    "Dhwoni": {
        "Mathematics": 95,
        "English": 88
    },

    "Rahul": {
        "Mathematics": 82,
        "English": 91
    }
}

for name, subjects in school.items():

    print("\nStudent:", name)

    for subject, mark in subjects.items():
        print(subject, ":", mark)


# ------------------------------------------------------------
# 24. LIST COMPREHENSION
# ------------------------------------------------------------
#
# Advanced compact form of a loop.
#
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [number ** 2 for number in numbers]

print(squares)


# ------------------------------------------------------------
# 25. CONDITIONAL LIST COMPREHENSION
# ------------------------------------------------------------

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)


# ------------------------------------------------------------
# 26. DICTIONARY COMPREHENSION
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)


# ------------------------------------------------------------
# 27. ENUMERATE + CONDITION
# ------------------------------------------------------------

marks = [95, 82, 67, 91, 45]

for index, mark in enumerate(marks, start=1):

    if mark >= 80:
        print("Subject", index, ":", mark, "Excellent")

    elif mark >= 50:
        print("Subject", index, ":", mark, "Passed")

    else:
        print("Subject", index, ":", mark, "Failed")


# ------------------------------------------------------------
# 28. ZIP + ENUMERATE
# ------------------------------------------------------------

subjects = [
    "Mathematics",
    "Bangla",
    "English",
    "History",
    "Geography"
]

marks = [95, 88, 91, 76, 84]

for number, (subject, mark) in enumerate(
    zip(subjects, marks),
    start=1
):
    print(number, subject, mark)


# ============================================================
#                    ADVANCED CHALLENGE 1
# ============================================================

# Create a program that analyzes:
#
# students = [
#     {"name": "Dhwoni", "marks": [95, 88, 92]},
#     {"name": "Rahul", "marks": [78, 85, 80]},
#     {"name": "Arjun", "marks": [65, 72, 69]}
# ]
#
# Calculate for EVERY student:
#
# 1. Total marks
# 2. Average marks
# 3. Highest mark
# 4. Lowest mark
# 5. Grade
#
# Do NOT use:
#
# sum()
# max()
# min()
#
# You must calculate them using FOR loops.


# ============================================================
#                    ADVANCED CHALLENGE 2
# ============================================================

# Create a program that searches for a student.
#
# Take the student's name using input().
#
# Search the following list:
#
# students = [
#     {"name": "Dhwoni", "age": 15},
#     {"name": "Rahul", "age": 16},
#     {"name": "Arjun", "age": 15}
# ]
#
# If found:
#
# Student Found
# Name: ...
# Age: ...
#
# Otherwise:
#
# Student Not Found
#
# Use:
#
# for
# if
# break
# else


# ============================================================
#                    ADVANCED CHALLENGE 3
# ============================================================

# Create a multiplication-table generator.
#
# Take:
#
# Starting number
# Ending number
#
# Example:
#
# Start: 2
# End: 5
#
# Generate tables for:
#
# 2
# 3
# 4
# 5
#
# Each table should contain 1–10.


# ============================================================
#                    ADVANCED CHALLENGE 4
# ============================================================

# Given:
#
# numbers = [12, 45, 7, 89, 34, 21, 90, 56]
#
# Find:
#
# 1. Highest number
# 2. Lowest number
# 3. Sum of all numbers
# 4. Number of even numbers
# 5. Number of odd numbers
#
# Do everything using FOR loops.
#
# Do NOT use:
#
# max()
# min()
# sum()
# len()


# ============================================================
#                    ADVANCED CHALLENGE 5
# ============================================================

# Create a student report generator.
#
# Use:
#
# students = [
#     {
#         "name": "Dhwoni",
#         "marks": [95, 88, 92, 85, 90]
#     },
#     {
#         "name": "Rahul",
#         "marks": [78, 85, 80, 75, 82]
#     },
#     {
#         "name": "Arjun",
#         "marks": [65, 72, 69, 70, 68]
#     }
# ]
#
# Using FOR loops, display:
#
# ==================================================
# Student: Dhwoni
# Total: ...
# Average: ...
# Highest: ...
# Lowest: ...
# Grade: ...
# ==================================================
#
# Do this for every student.
#
# This challenge combines:
#
# List
# Dictionary
# Nested list
# Nested loop
# if / elif / else
# arithmetic operators
# enumerate()
#
# ============================================================
#                        END
# ============================================================