# ============================================================
#              IF / ELSE CONDITIONAL STATEMENTS
# ============================================================
#
# Conditional statements allow Python to make decisions
# based on whether a condition is True or False.
#
# Main keywords:
#
# if
# elif
# else
#
# ============================================================


# ------------------------------------------------------------
# 1. BASIC IF
# ------------------------------------------------------------

age = 18

if age >= 18:
    print("You are an adult.")


# ------------------------------------------------------------
# 2. IF / ELSE
# ------------------------------------------------------------

age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# ------------------------------------------------------------
# 3. IF / ELIF / ELSE
# ------------------------------------------------------------

marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: C")


# ------------------------------------------------------------
# 4. COMPARISON OPERATORS
# ------------------------------------------------------------

number = 10

if number > 5:
    print("Greater than 5")

if number == 10:
    print("Number is 10")

if number != 20:
    print("Number is not 20")


# ------------------------------------------------------------
# 5. LOGICAL OPERATORS
# ------------------------------------------------------------

age = 20
has_id = True

if age >= 18 and has_id:
    print("Access allowed.")


age = 15

if age < 18 or not has_id:
    print("Access restricted.")


# ------------------------------------------------------------
# 6. NESTED IF
# ------------------------------------------------------------

age = 20
has_id = True

if age >= 18:

    if has_id:
        print("You can enter.")
    else:
        print("ID required.")

else:
    print("You are under 18.")


# ------------------------------------------------------------
# 7. MULTIPLE CONDITIONS
# ------------------------------------------------------------

marks = 92

if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Very Good")
elif marks >= 50:
    print("Good")
else:
    print("Needs improvement.")


# ------------------------------------------------------------
# 8. MEMBERSHIP WITH IF
# ------------------------------------------------------------

languages = ["Python", "Java", "C++"]

language = "Python"

if language in languages:
    print("Language found.")


# ------------------------------------------------------------
# 9. STRING CONDITIONS
# ------------------------------------------------------------

username = "Dhwoni"

if username:
    print("Username exists.")
else:
    print("Username is empty.")


# ------------------------------------------------------------
# 10. CHECKING DATA TYPES
# ------------------------------------------------------------

value = 100

if isinstance(value, int):
    print("Value is an integer.")


# ------------------------------------------------------------
# 11. CONDITIONAL EXPRESSION
# ------------------------------------------------------------

age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)


# Syntax:
#
# value_if_true if condition else value_if_false


# ------------------------------------------------------------
# 12. CHAINED COMPARISON
# ------------------------------------------------------------

age = 16

if 13 <= age <= 18:
    print("Teenager")


# Equivalent to:
#
# if age >= 13 and age <= 18:


# ------------------------------------------------------------
# 13. TRUTHY AND FALSY VALUES
# ------------------------------------------------------------

name = ""

if name:
    print("Name is available.")
else:
    print("Name is empty.")


# Empty strings, empty lists, empty dictionaries and 0
# are commonly treated as False in conditions.


# ------------------------------------------------------------
# 14. LIST CONDITION
# ------------------------------------------------------------

numbers = [10, 20, 30]

if numbers:
    print("The list contains data.")
else:
    print("The list is empty.")


# ------------------------------------------------------------
# 15. DICTIONARY CONDITION
# ------------------------------------------------------------

student = {
    "name": "Dhwoni",
    "marks": 95
}

if "marks" in student:
    print("Marks are available.")


# ------------------------------------------------------------
# 16. NESTED DATA
# ------------------------------------------------------------

student = {
    "name": "Dhwoni",
    "marks": {
        "math": 95,
        "science": 88
    }
}

if "marks" in student:
    if student["marks"]["math"] >= 90:
        print("Excellent in Mathematics.")


# ------------------------------------------------------------
# 17. PASS
# ------------------------------------------------------------

age = 16

if age >= 18:
    pass
else:
    print("Under 18.")


# pass means:
# "Do nothing for now."
#
# It is useful when you want to write the condition first
# and add the code later.


# ------------------------------------------------------------
# 18. REAL-WORLD EXAMPLE
# ------------------------------------------------------------

temperature = 35

if temperature >= 40:
    print("Very Hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Normal")
else:
    print("Cold")


# ============================================================
#                  ML / AI CONNECTION
# ============================================================

# Conditional logic is useful for:
#
# • Data filtering
# • Classification rules
# • Data validation
# • Feature engineering
# • Decision systems
# • Model output processing


score = 0.87

if score >= 0.90:
    result = "Very High Confidence"
elif score >= 0.70:
    result = "High Confidence"
else:
    result = "Low Confidence"

print(result)


# ============================================================
#                      IMPORTANT RULES
# ============================================================

# 1. A condition must produce True or False.
#
# 2. Use == for comparison.
#
#    if age == 18:
#        print("18")
#
# 3. Use = for assignment.
#
#    age = 18
#
# 4. Indentation is mandatory.
#
#    if age >= 18:
#        print("Adult")
#
# 5. Use elif for additional conditions.
#
# 6. else handles everything that didn't match above.


# ============================================================
#                       MINI CHALLENGE
# ============================================================

# Create a program that:
#
# 1. Stores a student's marks.
# 2. If marks >= 90 → "A+"
# 3. If marks >= 80 → "A"
# 4. If marks >= 70 → "B"
# 5. If marks >= 50 → "C"
# 6. Otherwise → "Fail"
#
# Bonus:
# Add another condition to check whether the student
# passed every required subject.