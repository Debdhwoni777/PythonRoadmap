# ============================================================
#                         PYTHON LIST
# ============================================================

# A list is an ordered, mutable collection.
# It can store multiple values of different data types.

numbers = [10, 20, 30, 40, 50]

print(numbers)
print(type(numbers))


# ------------------------------------------------------------
# 1. INDEXING
# ------------------------------------------------------------

print(numbers[0])       # First element
print(numbers[-1])      # Last element
print(numbers[1:4])     # Slicing


# ------------------------------------------------------------
# 2. MODIFYING A LIST
# ------------------------------------------------------------

numbers[0] = 100

print(numbers)


# ------------------------------------------------------------
# 3. ADDING ELEMENTS
# ------------------------------------------------------------

numbers.append(60)

numbers.insert(1, 15)

numbers.extend([70, 80, 90])

print(numbers)


# ------------------------------------------------------------
# 4. REMOVING ELEMENTS
# ------------------------------------------------------------

numbers.remove(15)

last = numbers.pop()

print(numbers)
print("Removed:", last)


# ------------------------------------------------------------
# 5. SEARCHING
# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

print(30 in numbers)
print(100 in numbers)

print(numbers.index(30))


# ------------------------------------------------------------
# 6. LENGTH
# ------------------------------------------------------------

print(len(numbers))


# ------------------------------------------------------------
# 7. SORTING
# ------------------------------------------------------------

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)

numbers.sort(reverse=True)

print(numbers)

# sorted() creates a new sorted list

numbers = [50, 10, 40, 20, 30]

new_numbers = sorted(numbers)

print(new_numbers)
print(numbers)


# ------------------------------------------------------------
# 8. REVERSE
# ------------------------------------------------------------

numbers.reverse()

print(numbers)


# ------------------------------------------------------------
# 9. LIST COMPREHENSION ⭐
# ------------------------------------------------------------

squares = [x ** 2 for x in range(1, 11)]

print(squares)


# With condition

even_numbers = [x for x in range(1, 21) if x % 2 == 0]

print(even_numbers)


# ------------------------------------------------------------
# 10. NESTED LIST
# ------------------------------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
print(matrix[1][2])


# ------------------------------------------------------------
# 11. LIST OF DIFFERENT DATA TYPES
# ------------------------------------------------------------

data = [
    "Dhwoni",
    16,
    5.7,
    True
]

print(data)


# ------------------------------------------------------------
# 12. UNPACKING
# ------------------------------------------------------------

person = ["Dhwoni", 16, "India"]

name, age, country = person

print(name)
print(age)
print(country)


# ------------------------------------------------------------
# 13. * UNPACKING
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print(first)
print(middle)
print(last)


# ------------------------------------------------------------
# 14. COPYING LISTS
# ------------------------------------------------------------

original = [1, 2, 3]

copy = original.copy()

copy.append(4)

print(original)
print(copy)


# ------------------------------------------------------------
# 15. LIST ALIASING ⚠️
# ------------------------------------------------------------

a = [1, 2, 3]

b = a

b.append(4)

print(a)
print(b)

# a and b refer to the same list.


# ============================================================
#                    ML / AI EXAMPLE
# ============================================================

# Dataset values

temperatures = [28.5, 30.2, 29.8, 31.1, 27.9]

average = sum(temperatures) / len(temperatures)

print("Average:", average)


# ============================================================
# IMPORTANT
# ============================================================

# List:
#
# Ordered
# Mutable
# Allows duplicates
# Indexed
# Can contain different data types
#
# Example:
#
# data = [10, 20, 30, 20]