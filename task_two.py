#generate a number btw 1 to 1000
#add the sum of the number






number = int(input("Enter a number btw 0 to 1000: "))

number_one = number % 10 
number_two = number % 100
number_three = number_two / 10 
number_four = number / 100 


sum = number_one + number_three + number_four
print(sum)