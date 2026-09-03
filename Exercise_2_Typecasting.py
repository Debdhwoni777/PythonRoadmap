# ============================================================
#             EXERCISE 2 — TYPECASTING & DATA
# ============================================================
#
# Topics Used:
# 1. Variables
# 2. Data Types
# 3. print()
# 4. Lists
# 5. Dictionaries
# 6. Operators
# 7. Typecasting
# 8. isinstance()
#
# ============================================================


# ------------------------------------------------------------
# 1. RAW DATA
# ------------------------------------------------------------

name = "Dhwoni"
age = "16"
height = "5.7"
marks = ["85", "92", "78", "95", "88"]


# ------------------------------------------------------------
# 2. TYPECASTING
# ------------------------------------------------------------

age = int(age)
height = float(height)

marks = [int(mark) for mark in marks]


# ------------------------------------------------------------
# 3. CALCULATIONS
# ------------------------------------------------------------

total_marks = sum(marks)
number_of_subjects = len(marks)

average_marks = total_marks / number_of_subjects

highest_marks = max(marks)
lowest_marks = min(marks)


# ------------------------------------------------------------
# 4. STUDENT DICTIONARY
# ------------------------------------------------------------

student = {
    "name": name,
    "age": age,
    "height": height,
    "marks": marks,
    "total_marks": total_marks,
    "average_marks": average_marks,
    "highest_marks": highest_marks,
    "lowest_marks": lowest_marks
}


# ------------------------------------------------------------
# 5. DISPLAY STUDENT INFORMATION
# ------------------------------------------------------------

print("=" * 50)
print("              STUDENT REPORT")
print("=" * 50)

print("Name           :", student["name"])
print("Age            :", student["age"])
print("Height         :", student["height"])
print("Marks          :", student["marks"])

print("-" * 50)

print("Total Marks    :", student["total_marks"])
print("Average Marks  :", student["average_marks"])
print("Highest Marks  :", student["highest_marks"])
print("Lowest Marks   :", student["lowest_marks"])

print("=" * 50)


# ------------------------------------------------------------
# 6. TYPE CHECKING
# ------------------------------------------------------------

print()
print("DATA TYPES")
print("-" * 30)

print("Name Type      :", type(name))
print("Age Type       :", type(age))
print("Height Type    :", type(height))
print("Marks Type     :", type(marks))


# ------------------------------------------------------------
# 7. isinstance()
# ------------------------------------------------------------

print()
print("TYPE VALIDATION")
print("-" * 30)

print("Age is integer :", isinstance(age, int))
print("Height is float:", isinstance(height, float))
print("Marks is list  :", isinstance(marks, list))


# ------------------------------------------------------------
# 8. SIMPLE OPERATOR PRACTICE
# ------------------------------------------------------------

next_year_age = age + 1

marks_difference = highest_marks - lowest_marks

print()
print("CALCULATIONS")
print("-" * 30)

print("Age next year  :", next_year_age)
print("Marks range    :", marks_difference)


# ============================================================
#                       CHALLENGE
# ============================================================

# Try to modify the program:
#
# 1. Add one more subject.
# 2. Change the marks.
# 3. Add "country" to the dictionary.
# 4. Calculate the percentage.
# 5. Find the number of subjects.
# 6. Check whether the average marks is a float.
#
# ============================================================