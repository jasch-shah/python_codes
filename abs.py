def absValue(num):
	if num < 0:
		return -num
	else:
		return num


def main():
	num1 = int(raw_input('Enter number 1'))
	print(absValue(num1))
	num2 = int(raw_input('Enter number 2'))
	print(absValue(num2))


if __name__ == '__main__':
	main()				