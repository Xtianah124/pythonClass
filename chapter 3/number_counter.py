passes = 0 
failures = 0
count = 0
number = int(input("Enter a number"))
int sentinal value = -1

for student in range(10):
	result = int(input('Enter result (1=pass, 2=fail): '))
	if result == 1:
	 passes = passes + 1
	else:
	 failures = failures + 1

	while passes != -1:
	total += passes
	grade += 1
	grade = int(input("Enter -1 to end:"))