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


marks = int(input("Enter Your marks: "))
print("Your marks is ", marks)

if marks >= 90:
    print("A+")

elif marks >= 80: 
    print("A")

elif marks >= 70:
    print("B")

elif marks >= 50:
    print("C")

else:
    print("Srroy, You are FALL")
