# ============================================================
#                  MATCH-CASE STATEMENTS
# ============================================================
#
# match-case is used when you want to compare one value
# against multiple possible patterns.
#
# Python 3.10+
#
# Main keywords:
# match
# case
#
# ============================================================


# ------------------------------------------------------------
# 1. BASIC MATCH-CASE
# ------------------------------------------------------------

day = 1

match day:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case 4:
        print("Thursday")

    case 5:
        print("Friday")

    case 6:
        print("Saturday")

    case 7:
        print("Sunday")


# ------------------------------------------------------------
# 2. DEFAULT CASE
# ------------------------------------------------------------

number = 10

match number:
    case 1:
        print("One")

    case 2:
        print("Two")

    case _:
        print("Something else")


# `_` means "anything else"


# ------------------------------------------------------------
# 3. MATCH-CASE WITH USER INPUT
# ------------------------------------------------------------

choice = input("Enter a number (1-3): ")

match choice:
    case "1":
        print("You selected One")

    case "2":
        print("You selected Two")

    case "3":
        print("You selected Three")

    case _:
        print("Invalid choice")


# ------------------------------------------------------------
# 4. MATCH-CASE WITH INTEGER INPUT
# ------------------------------------------------------------

choice = int(input("Enter a number (1-3): "))

match choice:
    case 1:
        print("You selected One")

    case 2:
        print("You selected Two")

    case 3:
        print("You selected Three")

    case _:
        print("Invalid choice")


# ------------------------------------------------------------
# 5. MATCH MULTIPLE VALUES
# ------------------------------------------------------------

day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")

    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")

    case _:
        print("Invalid day")


# `|` means OR


# ------------------------------------------------------------
# 6. MATCH WITH CONDITIONS
# ------------------------------------------------------------

marks = 85

match marks:
    case marks if marks >= 90:
        print("A+")

    case marks if marks >= 80:
        print("A")

    case marks if marks >= 70:
        print("B")

    case marks if marks >= 50:
        print("C")

    case _:
        print("FAIL")


# ------------------------------------------------------------
# 7. MATCHING STRINGS
# ------------------------------------------------------------

command = "start"

match command:
    case "start":
        print("Program started")

    case "stop":
        print("Program stopped")

    case "restart":
        print("Program restarted")

    case _:
        print("Unknown command")


# ------------------------------------------------------------
# 8. MATCHING TUPLES
# ------------------------------------------------------------

point = (10, 20)

match point:
    case (0, 0):
        print("Origin")

    case (x, 0):
        print("Point is on X-axis")

    case (0, y):
        print("Point is on Y-axis")

    case (x, y):
        print("Point:", x, y)


# ------------------------------------------------------------
# 9. MATCHING LIST PATTERNS
# ------------------------------------------------------------

numbers = [1, 2, 3]

match numbers:
    case []:
        print("Empty list")

    case [x]:
        print("One value:", x)

    case [x, y]:
        print("Two values:", x, y)

    case [x, y, z]:
        print("Three values:", x, y, z)

    case _:
        print("Other list")


# ------------------------------------------------------------
# 10. MATCHING DICTIONARIES
# ------------------------------------------------------------

student = {
    "name": "Dhwoni",
    "grade": "A"
}

match student:
    case {"grade": "A"}:
        print("Excellent student")

    case {"grade": "B"}:
        print("Good student")

    case {"grade": "C"}:
        print("Average student")

    case _:
        print("Grade not found")


# ============================================================
#                  MATCH-CASE VS IF-ELIF
# ============================================================

# if / elif is useful for conditions:

age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")


# match-case is useful when matching specific values:

choice = 2

match choice:
    case 1:
        print("Option 1")

    case 2:
        print("Option 2")

    case _:
        print("Other option")


# ============================================================
#                       IMPORTANT
# ============================================================

# match-case requires Python 3.10 or newer.
#
# The `_` case works like a default case.
#
# Example:
#
# match value:
#     case 1:
#         print("One")
#     case _:
#         print("Other")


# ============================================================
#                       MINI CHALLENGE
# ============================================================

# Create a simple calculator using match-case.
#
# Take:
#
# 1. First number
# 2. Operator (+, -, *, /)
# 3. Second number
#
# Example:
#
# Enter first number: 20
# Enter operator: *
# Enter second number: 5
#
# Output:
# Result: 100
#
# Operators:
#
# + → Addition
# - → Subtraction
# * → Multiplication
# / → Division
#
# Use:
#
# match operator:
#     case "+":
#         ...
#     case "-":
#         ...
#     case "*":
#         ...
#     case "/":
#         ...
#     case _:
#         ...