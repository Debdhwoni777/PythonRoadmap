# ============================================================
#                       PYTHON OPERATORS
# ============================================================

# Operators are special symbols or keywords used to perform
# operations on values and variables.


# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================

a = 10
b = 3

print(a + b)    # Addition        → 13
print(a - b)    # Subtraction     → 7
print(a * b)    # Multiplication  → 30
print(a / b)    # Division        → 3.333...
print(a // b)   # Floor Division  → 3
print(a % b)    # Modulus         → 1
print(a ** b)   # Power           → 1000


# ------------------------------------------------------------
# Operator precedence
# ------------------------------------------------------------

result = 10 + 5 * 2

print(result)   # 20

# () has the highest priority

result = (10 + 5) * 2

print(result)   # 30


# ============================================================
# 2. ASSIGNMENT OPERATORS
# ============================================================

x = 10

x += 5      # x = x + 5
print(x)    # 15

x -= 3      # x = x - 3
print(x)    # 12

x *= 2      # x = x * 2
print(x)    # 24

x /= 4      # x = x / 4
print(x)    # 6.0

x //= 2     # x = x // 2
print(x)    # 3.0

x %= 2      # x = x % 2
print(x)    # 1.0

x **= 3     # x = x ** 3
print(x)    # 1.0


# ============================================================
# 3. COMPARISON OPERATORS
# ============================================================

a = 10
b = 20

print(a == b)    # Equal to
print(a != b)    # Not equal to
print(a > b)     # Greater than
print(a < b)     # Less than
print(a >= b)    # Greater than or equal
print(a <= b)    # Less than or equal


# Comparison operators return True or False.


# ============================================================
# 4. LOGICAL OPERATORS
# ============================================================

age = 18
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)


# and → True if BOTH conditions are True
# or  → True if AT LEAST ONE condition is True
# not → Reverses True/False


# ============================================================
# 5. IDENTITY OPERATORS
# ============================================================

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)       # True
print(a is c)       # False

print(a is not c)   # True


# is     → Checks whether two variables refer to
#          the same object.
#
# is not → Checks whether they refer to different objects.


# ⚠️ Do NOT use "is" instead of "==" for normal value
# comparisons.


# ============================================================
# 6. MEMBERSHIP OPERATORS
# ============================================================

numbers = [10, 20, 30, 40]

print(20 in numbers)
print(100 in numbers)

print(20 not in numbers)
print(100 not in numbers)


# in     → Checks whether a value exists.
# not in → Checks whether a value does NOT exist.


# ------------------------------------------------------------
# Membership with strings
# ------------------------------------------------------------

text = "Python"

print("Py" in text)
print("Java" in text)


# ============================================================
# 7. BITWISE OPERATORS
# ============================================================

a = 5
b = 3

print(a & b)    # AND
print(a | b)    # OR
print(a ^ b)    # XOR
print(~a)       # NOT

print(a << 1)   # Left shift
print(a >> 1)   # Right shift


# Bitwise operators work at the binary/bit level.
#
# They are useful in:
# - Computer science
# - Binary data
# - Low-level programming
# - Optimization
# - Some ML/data-processing tasks


# ============================================================
# 8. CONDITIONAL EXPRESSION
# ============================================================

age = 18

status = "Adult" if age >= 18 else "Minor"

print(status)


# Syntax:
#
# value_if_true if condition else value_if_false


# ============================================================
# 9. OPERATOR PRECEDENCE
# ============================================================

result = 10 + 2 * 3 ** 2

print(result)

# Order:
#
# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -
# 5. Comparisons
# 6. not
# 7. and
# 8. or


# ============================================================
# 10. CHAINED COMPARISON ⭐
# ============================================================

age = 16

print(13 <= age <= 18)

# Same idea as:
#
# age >= 13 and age <= 18


# ============================================================
# 11. WALRUS OPERATOR := ⭐⭐⭐
# ============================================================

# The walrus operator assigns a value inside an expression.

if (length := len("Python")) > 5:
    print("Length:", length)


# ============================================================
# 12. OPERATOR OVERLOADING ⭐⭐⭐
# ============================================================

# Python allows operators to behave differently depending
# on the data type.

print(10 + 20)

print("Hello " + "Python")

print([1, 2] + [3, 4])

# + performs addition for numbers
# + performs concatenation for strings/lists


# ============================================================
#                   ML / AI EXAMPLE
# ============================================================

actual = 100
predicted = 92

error = actual - predicted
absolute_error = abs(error)

print("Error:", error)
print("Absolute Error:", absolute_error)


# ============================================================
#                       QUICK SUMMARY
# ============================================================

# Arithmetic:
# +   -   *   /   //   %   **
#
# Assignment:
# =   +=   -=   *=   /=   //=   %=   **=
#
# Comparison:
# ==   !=   >   <   >=   <=
#
# Logical:
# and   or   not
#
# Identity:
# is   is not
#
# Membership:
# in   not in
#
# Bitwise:
# &   |   ^   ~   <<   >>
#
# Conditional:
# x if condition else y
#
# Walrus:
# :=