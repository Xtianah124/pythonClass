passes = 0
failures = 0

for student in range(10):
 result = int(input("Enter result (1=pass, 2 =fail): "))

if result == 1:
  passes=+ 1
else:
  failure =+ 1

print("Number of student passed is", passes)
print("Number of student failed is ", failures)

if passes > 8:
 print("Bonus to instructor")