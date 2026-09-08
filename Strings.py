# ============================================================
#                      PYTHON STRINGS
# ============================================================

# A string is a sequence of characters.
# Strings are written inside quotes.

name = "Dhwoni"

print(name)
print(type(name))


# ------------------------------------------------------------
# 1. SINGLE, DOUBLE AND TRIPLE QUOTES
# ------------------------------------------------------------

single = 'Python'
double = "Python"

print(single)
print(double)

# Triple quotes are mainly used for multi-line strings
# and docstrings.

message = """
Python
Machine Learning
Artificial Intelligence
"""

print(message)


# ------------------------------------------------------------
# 2. STRING INDEXING
# ------------------------------------------------------------

text = "Python"

print(text[0])     # P
print(text[1])     # y
print(text[-1])    # n
print(text[-2])    # o


# Index positions:
#
# P  y  t  h  o  n
# 0  1  2  3  4  5
#-6 -5 -4 -3 -2 -1


# ------------------------------------------------------------
# 3. STRING SLICING
# ------------------------------------------------------------

text = "Python"

print(text[0:3])     # Pyt
print(text[2:])      # thon
print(text[:4])      # Pyth
print(text[:])       # Python

print(text[::2])     # Pto
print(text[::-1])    # nohtyP


# Syntax:
# string[start:stop:step]


# ------------------------------------------------------------
# 4. STRING LENGTH
# ------------------------------------------------------------

text = "Python"

print(len(text))


# ------------------------------------------------------------
# 5. STRING CONCATENATION
# ------------------------------------------------------------

first_name = "Dhwoni"
last_name = "Mondal1"

full_name = first_name + " " + last_name

print(full_name)


# ------------------------------------------------------------
# 6. STRING REPETITION
# ------------------------------------------------------------

print("Python " * 3)


# ------------------------------------------------------------
# 7. MEMBERSHIP OPERATORS
# ------------------------------------------------------------

text = "Python Programming"

print("Python" in text)
print("Java" in text)

print("Java" not in text)


# ------------------------------------------------------------
# 8. STRING METHODS
# ------------------------------------------------------------

text = "python programming"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())


# ------------------------------------------------------------
# 9. STRIPING WHITESPACE
# ------------------------------------------------------------

text = "   Python   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())


# ------------------------------------------------------------
# 10. REPLACE
# ------------------------------------------------------------

text = "I love Java"

new_text = text.replace("Java", "Python")

print(new_text)


# ------------------------------------------------------------
# 11. FIND
# ------------------------------------------------------------

text = "Python Programming"

print(text.find("Python"))
print(text.find("Java"))

# -1 means the text was not found.


# ------------------------------------------------------------
# 12. COUNT
# ------------------------------------------------------------

text = "banana"

print(text.count("a"))
print(text.count("na"))


# ------------------------------------------------------------
# 13. STARTSWITH / ENDSWITH
# ------------------------------------------------------------

filename = "python.py"

print(filename.startswith("python"))
print(filename.endswith(".py"))


# ------------------------------------------------------------
# 14. SPLIT
# ------------------------------------------------------------

text = "Python is powerful"

words = text.split()

print(words)

# Output:
# ['Python', 'is', 'powerful']


# ------------------------------------------------------------
# 15. JOIN
# ------------------------------------------------------------

words = ["Python", "is", "powerful"]

sentence = " ".join(words)

print(sentence)


# ------------------------------------------------------------
# 16. STRING IMMUTABILITY ⭐
# ------------------------------------------------------------

text = "Python"

# ❌ This is not allowed:
# text[0] = "J"

# Strings cannot be changed directly.
# Instead, create a new string.

text = "J" + text[1:]

print(text)


# ------------------------------------------------------------
# 17. F-STRINGS ⭐⭐⭐
# ------------------------------------------------------------

name = "Dhwoni"
age = 16

print(f"My name is {name} and I am {age} years old.")


# Expressions can also be used:

a = 10
b = 20

print(f"Sum = {a + b}")


# ------------------------------------------------------------
# 18. STRING FORMATTING
# ------------------------------------------------------------

price = 99.9999

print(f"Price: {price:.2f}")

# .2f → 2 digits after the decimal point


# ------------------------------------------------------------
# 19. ESCAPE SEQUENCES
# ------------------------------------------------------------

print("Hello\nPython")

print("Name:\tDhwoni")

print("He said, \"Hello!\"")

print("C:\\Python\\Projects")


# ------------------------------------------------------------
# 20. RAW STRINGS
# ------------------------------------------------------------

path = r"C:\Users\Dhwoni\Desktop"

print(path)

# r"" prevents most backslashes from being treated
# as escape sequences.


# ------------------------------------------------------------
# 21. STRING COMPARISON
# ------------------------------------------------------------

print("apple" == "apple")
print("apple" == "Apple")

print("Python" != "Java")


# ------------------------------------------------------------
# 22. STRING CASE CONVERSION
# ------------------------------------------------------------

text = "PyThOn"

print(text.lower())
print(text.upper())


# Useful for case-insensitive comparisons:

user_input = "PYTHON"

if user_input.lower() == "python":
    print("Correct!")


# ------------------------------------------------------------
# 23. CHECKING STRING CONTENT
# ------------------------------------------------------------

text = "Python123"

print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print(text.islower())
print(text.isupper())


# ------------------------------------------------------------
# 24. STRING PARTITION
# ------------------------------------------------------------

email = "dhwoni@example.com"

username, separator, domain = email.partition("@")

print("Username:", username)
print("Domain:", domain)


# ------------------------------------------------------------
# 25. CONVERTING OTHER TYPES TO STRING
# ------------------------------------------------------------

age = 16

age_text = str(age)

print(age_text)
print(type(age_text))


# ============================================================
#                  STRING + USER INPUT
# ============================================================

name = input("Enter your name: ")

print(f"Welcome, {name}!")


# ============================================================
#                  ML / AI CONNECTION
# ============================================================

# In real projects, strings are often used for:
#
# • Names
# • Text data
# • File paths
# • URLs
# • JSON data
# • User input
# • Natural Language Processing (NLP)
# • Dataset labels


# Example:

text = "Python is powerful"

words = text.lower().split()

print(words)


# ============================================================
#                    IMPORTANT SUMMARY
# ============================================================

# String:
# str
#
# Indexing:
# text[0]
#
# Slicing:
# text[start:stop:step]
#
# Length:
# len(text)
#
# Concatenation:
# "Hello" + "Python"
#
# Repeat:
# "Hi " * 3
#
# Membership:
# "Py" in text
#
# Formatting:
# f"Hello {name}"
#
# Common methods:
# upper()
# lower()
# title()
# strip()
# replace()
# find()
# count()
# split()
# join()
# startswith()
# endswith()


# ============================================================
#                       MINI CHALLENGE
# ============================================================

# Create a program that:
#
# 1. Takes the user's full name.
# 2. Removes unnecessary spaces.
# 3. Converts the name to title case.
# 4. Prints the number of characters.
# 5. Prints the name in uppercase.
# 6. Prints the first and last character.
#
# Example:
#
# Input:
#    dhwoni mondal
#
# Output:
#    Name       : Dhwoni Mondal
#    Characters : 13
#    Uppercase  : DHWONI MONDAL
#    First      : D
#    Last       : A