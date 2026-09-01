# ============================================================
#                      PYTHON DICTIONARY
# ============================================================

# A dictionary stores data as KEY : VALUE pairs.

student = {
    "name": "Dhwoni",
    "age": 16,
    "country": "India"
}

print(student)
print(type(student))


# ------------------------------------------------------------
# 1. ACCESSING VALUES
# ------------------------------------------------------------

print(student["name"])
print(student["age"])


# ------------------------------------------------------------
# 2. get() ⭐
# ------------------------------------------------------------

print(student.get("name"))

# If the key doesn't exist:git --version
print(student.get("school"))

# No error — returns None.


# ------------------------------------------------------------
# 3. ADDING DATA
# ------------------------------------------------------------

student["school"] = "ABC School"

print(student)


# ------------------------------------------------------------
# 4. MODIFYING DATA
# ------------------------------------------------------------

student["age"] = 17

print(student)


# ------------------------------------------------------------
# 5. REMOVING DATA
# ------------------------------------------------------------

student.pop("country")

print(student)


# ------------------------------------------------------------
# 6. KEYS / VALUES / ITEMS
# ------------------------------------------------------------

print(student.keys())

print(student.values())

print(student.items())


# ------------------------------------------------------------
# 7. LOOP THROUGH DICTIONARY
# ------------------------------------------------------------

student = {
    "name": "Dhwoni",
    "age": 16,
    "country": "India"
}

for key, value in student.items():
    print(key, ":", value)


# ------------------------------------------------------------
# 8. CHECKING KEYS
# ------------------------------------------------------------

print("name" in student)

print("school" in student)


# ------------------------------------------------------------
# 9. DICTIONARY COMPREHENSION ⭐
# ------------------------------------------------------------

squares = {
    x: x ** 2
    for x in range(1, 6)
}

print(squares)


# With condition

even_squares = {
    x: x ** 2
    for x in range(1, 11)
    if x % 2 == 0
}

print(even_squares)


# ------------------------------------------------------------
# 10. NESTED DICTIONARY ⭐
# ------------------------------------------------------------

student = {
    "name": "Dhwoni",
    "marks": {
        "math": 95,
        "physics": 90,
        "computer": 98
    }
}

print(student["marks"]["computer"])


# ------------------------------------------------------------
# 11. LIST + DICTIONARY ⭐⭐⭐
# ------------------------------------------------------------

students = [
    {
        "name": "Dhwoni",
        "age": 16,
        "marks": 95
    },

    {
        "name": "Rahul",
        "age": 17,
        "marks": 91
    },

    {
        "name": "Ananya",
        "age": 16,
        "marks": 97
    }
]

for student in students:
    print(student["name"], student["marks"])


# ------------------------------------------------------------
# 12. SAFE ACCESS
# ------------------------------------------------------------

student = {
    "name": "Dhwoni",
    "age": 16
}

school = student.get("school", "Not Available")

print(school)


# ------------------------------------------------------------
# 13. MERGING DICTIONARIES
# ------------------------------------------------------------

person = {
    "name": "Dhwoni",
    "age": 16
}

location = {
    "country": "India",
    "state": "West Bengal"
}

combined = person | location

print(combined)


# ============================================================
#                    ML / AI EXAMPLE
# ============================================================

model_info = {
    "model": "Linear Regression",
    "version": 1,
    "features": ["age", "income", "experience"],
    "accuracy": 0.92
}

print(model_info["model"])
print(model_info["features"])
print(model_info["accuracy"])


# ============================================================
# IMPORTANT
# ============================================================

# Dictionary:
#
# Stores KEY : VALUE
# Mutable
# Keys must be unique
# Fast lookup by key
# Can contain nested dictionaries/lists
#
# Example:
#
# user = {
#     "name": "Dhwoni",
#     "age": 16
# }