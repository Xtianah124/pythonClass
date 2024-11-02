passes = 0; 
failures = 0;
counter = 0;

for student in range(10):
	result = int(input("Enter number 1 or 2 "));
	if result == 1:
		passes = passes + 1
	else:	
		failure = failure + 1

	while counter != -1:
		total_pass = result + 1
		print(total_pass)