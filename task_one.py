psudocode
#prompt user to enter a number
#collect number
#save number as number_one
#promt user to enter a number
#collect number
#save number as number_two
#sum both numbers
#prompt the user to enter sum
#collect sum 
#save as user_input
#check: if user_input is equal to sum
#print True if correct
#print False if wrong
#display result


number_one = int(input("Enter a number: "))
number_two = int(input("Enter a number: "))

sum = number_one + number_two

user_input = int(input("Enter the sum: "))
if(user_input == sum):
	print(True)
else: 
	print(False)