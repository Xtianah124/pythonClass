def display_menu():
	print = """ 
Welcome dear customer, 
	Enter a number to continue -> 

	1. Create an account
	2. Sign in
	3. Deposit money
	4. Withdraw money
	5. Check account balance
	6. Transfer from one account to another
	7. Change 
	8. Close account
"""

	print(menu)
	user_input = int(input("Enter a number: ")) 

	match(user_input):

		case 1: create_an_account()
		case 2: sign_in()
		case 3: deposit_money()
		case 4: withdraw()
		case 5: check_account_balance()
		case 6: transfer_from_one_account_to_another()
		case 7: change_pin()
		case 8: close_account()
		case 9: system.exit(3)
	


def create_an_account():
	
	first_name = input("what's your first name: ")

	last_name = input("Enter your last name: ")

	date_of_birth = input("Enter date of birth: ")

	pin = int(input("Enter your pin: "))
	
	displayMenu()
	


def sign_in():
	
	first_name = input("what's your first name: ")
	
	last_name = input("Enter your last name: ")

	pin = int(input("Enter your pin: "))
	



def deposit_money():

	amount_to_deposit = int(input("Enter amount to deposit: "))
	
	transaction_pin = int(input("Enter your transaction pin: "))

	print("Successfully transferred "+amount)




def withdraw():

	amount = int(input("Enter amount: "))

	transaction_pin = int(input("Enter transaction pin: "))

	print("Withdraw successful")


def check_account_balance():

	account_number = int(input("Enter your account number: "))

	transaction_pin = int(input("Enter transaction pin: "))

	print("Your account balance is")


def transfer_from_one_account_to_another():

	account_number = int(input("Enter account number: "))

	amount_to_transfer = int(input("Enter amount to transfer: "))
	
	transaction_pin = int(input("Enter transaction pin: "))
	
	print("Transaction successful")



def change_pin():

	current_pin = int(input("Input current pin: "))

	new_pin = int(input("Input new pin: "))

	confirm_pin = int(input("Confirm new pin: "))

	print("pin successfully changed")



def close_account():
	
	close = input("Dear customer, are you sure you want to close this account: ")
	
	while(true):

		account_details = input("provide account details: ")

		funds = input("Transfer funds: ")

		reason = input("Reasons for closing account: ")
		break

print(display_menu)
	