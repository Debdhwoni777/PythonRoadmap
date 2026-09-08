# ============================================================
#                TAKING USER INPUT IN PYTHON
# ============================================================

# input() is used to take data from the user.
#
# IMPORTANT:
# input() ALWAYS returns a string (str).
#
# Example:
# name = input("Enter your name: ")


# ------------------------------------------------------------
# 1. BASIC USER INPUT
# ------------------------------------------------------------

name = input("Enter your name: ")

print("Hello,", name)


# ------------------------------------------------------------
# 2. CHECKING THE INPUT TYPE
# ------------------------------------------------------------

name = input("Enter your name: ")

print("Value:", name)
print("Data Type:", type(name))

# Output type will be:
# <class 'str'>


# ------------------------------------------------------------
# 3. TAKING INTEGER INPUT
# ------------------------------------------------------------

age = int(input("Enter your age: "))

print("Your age is:", age)
print("Data Type:", type(age))


# ------------------------------------------------------------
# 4. TAKING FLOAT INPUT
# ------------------------------------------------------------

height = float(input("Enter your height: "))

print("Your height is:", height)
print("Data Type:", type(height))


# ------------------------------------------------------------
# 5. TAKING MULTIPLE INPUTS
# ------------------------------------------------------------

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("Hello,", first_name, last_name)