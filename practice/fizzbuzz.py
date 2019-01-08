from __future__ import print_function

for num in range(1, 50):
	string = ""
	if num % 3 == 0:
		string = string + "Fizz"
	if num % 5 == 0:
		string = string + "Buzz"
	if num % 5 != 0 and num % 3 != 0:
		string = string + str(num)
	print(string, end=' ')
		 		