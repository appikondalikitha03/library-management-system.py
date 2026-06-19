import random

# List of students
students = ["Ravi", "Priya", "Arjun", "Sneha", "Kiran"]

# Performance grades
grades = ["Excellent", "Very Good", "Good", "Average", "Needs Improvement"]

# Select a random student
student = random.choice(students)

# Assign a random performance grade
performance = random.choice(grades)

print("===== STUDENT PERFORMANCE REPORT =====")
print("Student Name :", student)
print("Performance  :", performance)

if performance == "Excellent":
    print("Remark       : Outstanding performance!")
elif performance == "Very Good":
    print("Remark       : Keep up the good work!")
elif performance == "Good":
    print("Remark       : Doing well, can improve further.")
elif performance == "Average":
    print("Remark       : Needs more practice.")
else:
    print("Remark       : Requires extra attention and effort.")