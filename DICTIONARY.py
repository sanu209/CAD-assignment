# Student marks dictionary
students = {
    "Aman": 85,
    "Riya": 90,
    "Sohan": 78
}

name = input("Enter student name: ")

if name in students:
    print("Marks:", students[name])
else:
    print("Student not found")

# Add and display dictionary items
d = {}

n = int(input("How many items? "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

print("Dictionary:", d)
