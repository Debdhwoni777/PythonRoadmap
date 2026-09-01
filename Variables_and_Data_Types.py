# ============================================================
#                 PYTHON VARIABLES & DATA TYPES
# ============================================================

# A variable is a name used to store a value.
#
# Syntax:
# variable_name = value


# ------------------------------------------------------------
# 1. CREATING VARIABLES
# ------------------------------------------------------------

name = "Dhwoni"
age = 16
height = 5.7

print(name)
print(age)
print(height)


# ------------------------------------------------------------
# 2. VARIABLES CAN STORE DIFFERENT TYPES OF DATA
# ------------------------------------------------------------

name = "Dhwoni"       # String
age = 16              # Integer
height = 5.7          # Float
is_learning = True    # Boolean

print(name)
print(age)
print(height)
print(is_learning)


# ------------------------------------------------------------
# 3. MAIN PYTHON DATA TYPES
# ------------------------------------------------------------

# str  → String   → Text
# int  → Integer  → Whole numbers
# float → Decimal numbers
# bool → Boolean   → True / False


# ------------------------------------------------------------
# 4. STRING — str
# ------------------------------------------------------------

name = "Dhwoni"
country = "India"

print(name)
print(country)

print(type(name))


# ------------------------------------------------------------
# 5. INTEGER — int
# ------------------------------------------------------------

age = 16
marks = 95
year = 2026

print(age)
print(marks)
print(year)

print(type(age))


# ------------------------------------------------------------
# 6. FLOAT — float
# ------------------------------------------------------------

height = 5.7
price = 99.99
pi = 3.14159

print(height)
print(price)
print(pi)

print(type(price))


# ------------------------------------------------------------
# 7. BOOLEAN — bool
# ------------------------------------------------------------

is_student = True
is_raining = False

print(is_student)
print(is_raining)

print(type(is_student))


# ------------------------------------------------------------
# 8. CHECKING THE DATA TYPE
# ------------------------------------------------------------

x = 100

print(type(x))


# Examples:

print(type("Hello"))     # str
print(type(100))         # int
print(type(10.5))        # float
print(type(True))        # bool


# ------------------------------------------------------------
# 9. MULTIPLE VARIABLES
# ------------------------------------------------------------

name, age, country = "Dhwoni", 16, "India"

print(name)
print(age)
print(country)


# ------------------------------------------------------------
# 10. SAME VALUE TO MULTIPLE VARIABLES
# ------------------------------------------------------------

x = y = z = 10

print(x)
print(y)
print(z)


# ------------------------------------------------------------
# 11. VARIABLE VALUES CAN CHANGE
# ------------------------------------------------------------

age = 16

print(age)

age = 17

print(age)


# ------------------------------------------------------------
# 12. VARIABLE NAMING RULES
# ------------------------------------------------------------

# ✅ Correct:

student_name = "Dhwoni"
age2 = 16
_my_variable = 100


# ❌ Incorrect:

# 2age = 16
# student-name = "Dhwoni"
# class = "Python"


# Rules:
#
# 1. Cannot start with a number.
# 2. Can contain letters, numbers and underscore (_).
# 3. Cannot use Python keywords.
# 4. Variable names are case-sensitive.


# ------------------------------------------------------------
# 13. CASE SENSITIVE
# ------------------------------------------------------------

name = "Dhwoni"
Name = "Python"

print(name)
print(Name)

# name and Name are different variables.


# ------------------------------------------------------------
# 14. TYPE CONVERSION
# ------------------------------------------------------------

# Converting one data type into another.

age = "16"

print(age)
print(type(age))

age = int(age)

print(age)
print(type(age))


# More examples:

x = 10
y = float(x)

print(y)
print(type(y))


number = 100
text = str(number)

print(text)
print(type(text))


# ============================================================
#                       QUICK SUMMARY
# ============================================================

# Variable → Stores a value
#
# str   → "Hello"
# int   → 100
# float → 10.5
# bool  → True / False
#
# type() → Checks the data type
#
# int()   → Converts to integer
# float() → Converts to float
# str()   → Converts to string
# bool()  → Converts to boolean


# ============================================================
#                      MINI PRACTICE
# ============================================================

# Create variables for:
#
# Your name
# Your age
# Your school
# Your favorite subject
# Your Python learning status
#
# Then print them and use type() to check their data types.