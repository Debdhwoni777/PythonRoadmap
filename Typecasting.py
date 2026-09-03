# ============================================================
#                    PYTHON TYPECASTING
# ============================================================
#
# Typecasting means converting a value from one data type
# into another data type.
#
# Common functions:
# int()    -> Integer
# float()  -> Floating-point number
# str()    -> String
# bool()   -> Boolean
# list()   -> List
# tuple()  -> Tuple
# set()    -> Set
#
# ============================================================


# ------------------------------------------------------------
# 1. BASIC TYPECASTING
# ------------------------------------------------------------

number = 10

print(number)
print(type(number))

decimal = float(number)

print(decimal)
print(type(decimal))


# ------------------------------------------------------------
# 2. STRING TO NUMBER
# ------------------------------------------------------------

age = "16"

age = int(age)

print(age)
print(type(age))


price = "99.50"

price = float(price)

print(price)
print(type(price))


# ------------------------------------------------------------
# 3. NUMBER TO STRING
# ------------------------------------------------------------

number = 100

text = str(number)

print(text)
print(type(text))


# ------------------------------------------------------------
# 4. INTEGER <-> FLOAT
# ------------------------------------------------------------

x = 10

y = float(x)

print(y)          # 10.0
print(type(y))    # float


value = 10.99

result = int(value)

print(result)     # 10
print(type(result))


# ⚠️ int() removes the decimal part.
# It does NOT round the number.


# ------------------------------------------------------------
# 5. BOOLEAN TYPECASTING
# ------------------------------------------------------------

print(bool(1))        # True
print(bool(0))        # False

print(bool(100))      # True
print(bool(-5))       # True

print(bool(""))       # False
print(bool("Hello"))  # True


# ------------------------------------------------------------
# 6. IMPORTANT BOOLEAN RULE
# ------------------------------------------------------------

# These values are generally considered False:

print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(None))

# Most other values are True.


# ------------------------------------------------------------
# 7. STRING TO BOOLEAN
# ------------------------------------------------------------

value = "False"

print(bool(value))

# Output:
# True
#
# Because "False" is a non-empty string.
#
# bool("False") != False


# ------------------------------------------------------------
# 8. CONVERTING COLLECTIONS
# ------------------------------------------------------------

numbers = [1, 2, 3, 4]

my_tuple = tuple(numbers)
my_set = set(numbers)

print(my_tuple)
print(type(my_tuple))

print(my_set)
print(type(my_set))


# ------------------------------------------------------------
# 9. TUPLE TO LIST
# ------------------------------------------------------------

data = (10, 20, 30)

data = list(data)

print(data)
print(type(data))


# ------------------------------------------------------------
# 10. STRING TO LIST
# ------------------------------------------------------------

text = "Python"

characters = list(text)

print(characters)

# Output:
# ['P', 'y', 't', 'h', 'o', 'n']


# ------------------------------------------------------------
# 11. STRING TO SET
# ------------------------------------------------------------

text = "banana"

unique_characters = set(text)

print(unique_characters)

# Duplicate characters are removed.


# ------------------------------------------------------------
# 12. DICTIONARY TYPECASTING
# ------------------------------------------------------------

pairs = [
    ("name", "Dhwoni"),
    ("age", 16)
]

student = dict(pairs)

print(student)
print(type(student))


# ------------------------------------------------------------
# 13. DICTIONARY KEYS / VALUES
# ------------------------------------------------------------

student = {
    "name": "Dhwoni",
    "age": 16
}

keys = list(student.keys())
values = list(student.values())

print(keys)
print(values)


# ------------------------------------------------------------
# 14. NUMERIC STRING CONVERSION
# ------------------------------------------------------------

x = "101"

decimal_number = int(x)

print(decimal_number + 10)


# ------------------------------------------------------------
# 15. BASE CONVERSION ⭐
# ------------------------------------------------------------

binary = "1010"

number = int(binary, 2)

print(number)

# Binary 1010 = Decimal 10


hexadecimal = "FF"

number = int(hexadecimal, 16)

print(number)

# FF = Decimal 255


# ------------------------------------------------------------
# 16. FLOATING-POINT CONVERSION
# ------------------------------------------------------------

x = "3.14159"

number = float(x)

print(number)


# ------------------------------------------------------------
# 17. ROUNDING vs TYPECASTING
# ------------------------------------------------------------

number = 10.89

print(int(number))      # 10
print(round(number))     # 11
print(round(number, 1))  # 10.9

# int()    -> removes decimal part
# round()  -> rounds the number


# ------------------------------------------------------------
# 18. TYPECASTING WITH EXPRESSIONS
# ------------------------------------------------------------

x = "10"
y = "20"

result = int(x) + int(y)

print(result)

# Output:
# 30


# ------------------------------------------------------------
# 19. TYPECASTING INSIDE EXPRESSIONS
# ------------------------------------------------------------

price = "100"
quantity = "3"

total = int(price) * int(quantity)

print("Total:", total)


# ------------------------------------------------------------
# 20. NESTED TYPECASTING ⭐
# ------------------------------------------------------------

data = "10"

result = float(int(data))

print(result)

# "10" -> int -> float
# 10   -> 10.0


# ============================================================
#              TYPECASTING vs TYPE CONVERSION
# ============================================================

# Typecasting is commonly used to describe explicitly
# converting one type into another.
#
# Example:

age = int("16")

print(age)


# ============================================================
#                 TYPE CHECKING
# ============================================================

value = 100

print(type(value))

print(isinstance(value, int))

# type()      -> gives the exact type
# isinstance() -> checks whether an object belongs to a type


# ------------------------------------------------------------
# isinstance() WITH MULTIPLE TYPES
# ------------------------------------------------------------

value = 10.5

print(isinstance(value, (int, float)))

# True


# ============================================================
#                  SAFE TYPECASTING
# ============================================================

# Invalid conversion can cause ValueError.

# number = int("Python")   # ValueError


# A safer approach:

value = "Python"

try:
    number = int(value)
    print(number)

except ValueError:
    print("Cannot convert to integer.")


# ============================================================
#               TYPECASTING + USER INPUT
# ============================================================

# input() always returns a string.

# age = input("Enter your age: ")
# print(type(age))


# Convert the input:

# age = int(input("Enter your age: "))
# print(type(age))


# ============================================================
#                 ML / AI CONNECTION
# ============================================================

# Machine-learning data often needs consistent data types.

temperature = "32.5"
temperature = float(temperature)

print(temperature)
print(type(temperature))


# Example of converting several values:

raw_data = ["10", "20", "30", "40"]

numbers = [int(value) for value in raw_data]

print(numbers)

# ['10', '20', '30', '40']
#          ↓
# [10, 20, 30, 40]


# ============================================================
#                       QUICK SUMMARY
# ============================================================

# int(x)       -> Convert to integer
# float(x)     -> Convert to float
# str(x)       -> Convert to string
# bool(x)      -> Convert to boolean
# list(x)      -> Convert to list
# tuple(x)     -> Convert to tuple
# set(x)       -> Convert to set
# dict(x)      -> Convert to dictionary
#
# type(x)      -> Check exact type
# isinstance() -> Check whether value is a type
#
# int("101", 2) -> Convert binary string to integer
#
# ============================================================