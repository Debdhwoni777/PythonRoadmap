# ============================================================
#                         PYTHON PRINT()
# ============================================================

# print() is a built-in Python function.
# It is used to display/output information on the screen.


# ------------------------------------------------------------
# 1. PRINT TEXT
# ------------------------------------------------------------

print("Hello, Python!")

print("India is my country")


# ------------------------------------------------------------
# 2. PRINT NUMBERS
# ------------------------------------------------------------

print(10)

print(3.14)

print(2026)


# ------------------------------------------------------------
# 3. PRINT MULTIPLE VALUES
# ------------------------------------------------------------

print("My name is", "Dhwoni")

print("Age:", 16)

print("Python", "is", "easy")


# ------------------------------------------------------------
# 4. PRINT VARIABLES
# ------------------------------------------------------------

name = "Dhwoni"
age = 16

print(name)
print(age)

print("Name:", name)
print("Age:", age)


# ------------------------------------------------------------
# 5. SEPARATOR — sep
# ------------------------------------------------------------

print("Python", "Java", "C", sep=" | ")

# Output:
# Python | Java | C


# ------------------------------------------------------------
# 6. END — end
# ------------------------------------------------------------

print("Hello", end=" ")
print("World")

# Output:
# Hello World


print("Python", end=" → ")
print("ML", end=" → ")
print("AI")


# ------------------------------------------------------------
# 7. USING ESCAPE SEQUENCES
# ------------------------------------------------------------

print("Hello\nPython")

print("Name:\tDhwoni")


# ------------------------------------------------------------
# 8. PRINT QUOTES
# ------------------------------------------------------------

print("He said, \"Hello!\"")

print('It\'s Python')


# ------------------------------------------------------------
# 9. PRINT CALCULATIONS
# ------------------------------------------------------------

print(10 + 5)

print(10 - 5)

print(10 * 5)

print(10 / 5)


# ------------------------------------------------------------
# 10. PRINT EXPRESSIONS
# ------------------------------------------------------------

x = 10
y = 20

print("Sum =", x + y)

print("Product =", x * y)


# ============================================================
#                         REMEMBER
# ============================================================

# print() → Displays output on the screen
#
# sep → Controls the separator between values
# end → Controls what happens at the end of print()
#
# Example:
# print("Hello", "World", sep=" - ", end="!")
#
# Output:
# Hello - World!


# ============================================================
#                      MINI PRACTICE
# ============================================================

# Try to create this output:
#
# Name: Dhwoni
# Goal: ML & AI Engineer
# Python → Machine Learning → AI
#
# Use print(), sep and end.