# CAD-assignment
# 1.Write a code to find even numbers in an array (list)
number = [1, 2, 3, 4, 5, 6]

for i in number:
    if i % 2 == 0:
        print(i)
#2. Write a code to reverse an array without using any function
number = [1, 2, 3, 4, 5]
rev = []

for i in range(len(number)-1, -1, -1):
    rev.append(number[i])

print(rev)

#3. Write a program to check whether an element is present in a list or not
lst = [10, 20, 30, 40]
key = 30
found = False

for i in lst:
    if i == key:
        found = True
        break

if found:
    print("Element is present")
else:
    print("Element is not present")
4.# Write a program to remove duplicate elements from a list
lst = [1, 2, 2, 3, 4, 4, 5]
unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

print(unique)

#5.Find max and min value from a tuple without using any in-built function
t = (5, 2, 9, 1, 7)

max_val = t[0]
min_val = t[0]

for i in t:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print("Maximum:", max_val)
print("Minimum:", min_val)


