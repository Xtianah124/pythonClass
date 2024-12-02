#prompt user to enter three integers and display them in increasing order 
#prompt user to enter a number
#collect number 
#save number as number_one
#promt user to enter a number
#collect number
#save number as number_two
#prompt user to enter a number
#collect  
#save number as number_three
#





number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))
number_three = int(input("Enter third number: "))

if number_one < number_two & number_one < number_two:
	print(number_one)
elif number_two > number_one & number_two < number_three:
	print(number_two)
else: number_three > number_two & number_three > number_one
print(number_three)