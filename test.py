print("===== Student Grade Manager =====")

# Get student name
name = input("mohame siddiq: ")

# Get marks
english = float(input("Enter English marks: "))
science = float(input("Enter Science marks: "))
social = float(input("Enter Social marks: "))
maths = float(input("Enter Maths marks: "))

# Calculate total and average
total = english + science + social + maths
average = total / 4

# Calculate grade
if average >= 90:
    grade = "
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Display student report
print("\n===== Student Report =====")
print("Student Name:", name)
print("English:", english)
print("Science:", science)
print("Social:", social)
print("Maths:", maths)
print("-------------------------")
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)