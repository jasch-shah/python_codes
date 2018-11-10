def factorial(number):
	if number < 0:
		print('Invalid entry ! Cannot find factorial of negative number')
	if number == 0 or number == 1:
		return 1
	else:
		return number * factorial(number - 1)

	
if __name__ == '__main__':
	userInput = int(input('Enter number to find the factorial of :'))
	print(factorial(userInput))				