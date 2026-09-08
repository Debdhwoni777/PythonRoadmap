# ============================================================
#             EXERCISE 3 — STUDENT PERFORMANCE
# ============================================================

# Concepts Used:
# Variables
# Data Types
# input()
# Typecasting
# Lists
# Dictionaries
# Operators
# if / elif / else
# Built-in functions


# ------------------------------------------------------------
# 1. STUDENT INFORMATION
# ------------------------------------------------------------

name = input("Enter your name: ")
age = int(input("Enter your age: "))


# ------------------------------------------------------------
# 2. SUBJECT MARKS
# ------------------------------------------------------------

Mathematics = int(input("Enter your Mathematics marks: "))
Bangla = int(input("Enter your Bangla marks: "))
English = int(input("Enter your English marks: "))
History = int(input("Enter your History marks: "))
Geography = int(input("Enter your Geography marks: "))


# ------------------------------------------------------------
# 3. STORE MARKS IN A LIST
# ------------------------------------------------------------

marks = [Mathematics, Bangla, English, History, Geography]


# ------------------------------------------------------------
# 4. CALCULATIONS
# ------------------------------------------------------------

Total_Marks = sum(marks)

Average_Marks = Total_Marks / len(marks)

Highest_marks = max(marks)

Lowest_marks = min(marks)


# ------------------------------------------------------------
# 5. CREATE STUDENT DICTIONARY
# ------------------------------------------------------------

student = {
    "name": name,
    "age": age,
    "marks": marks,
    "total_marks": Total_Marks,
    "average_marks": Average_Marks,
    "highest_marks": Highest_marks,
    "lowest_marks": Lowest_marks,
    "grade": "",
    "result": ""
}


# ------------------------------------------------------------
# 6. CALCULATE GRADE
# ------------------------------------------------------------

if Average_Marks >= 90:
    grade = "A+"

elif Average_Marks >= 80:
    grade = "A"

elif Average_Marks >= 70:
    grade = "B"

elif Average_Marks >= 50:
    grade = "C"

else:
    grade = "FAIL"


# ------------------------------------------------------------
# 7. SUBJECT-WISE PASS CHECK
# ------------------------------------------------------------

if Mathematics >= 33 and Bangla >= 33 and English >= 33 and History >= 33 and Geography >= 33:
    result = "PASS"
else:
    result = "FAIL"


# ------------------------------------------------------------
# 8. STORE GRADE AND RESULT IN DICTIONARY
# ------------------------------------------------------------

student["grade"] = grade
student["result"] = result


# ------------------------------------------------------------
# 9. DISPLAY STUDENT REPORT
# ------------------------------------------------------------

print()
print("=" * 50)
print("             STUDENT PERFORMANCE")
print("=" * 50)

print("Name             :", student["name"])
print("Age              :", student["age"])
print("Marks            :", student["marks"])

print("-" * 50)

print("Total Marks      :", student["total_marks"])
print("Average Marks    :", student["average_marks"])
print("Highest Marks    :", student["highest_marks"])
print("Lowest Marks     :", student["lowest_marks"])

print("-" * 50)

print("Grade            :", student["grade"])
print("Result           :", student["result"])

print("=" * 50)


# ============================================================
#                        END
# ============================================================