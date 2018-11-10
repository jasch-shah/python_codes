def main():
	print("Illustration of Chaos Function")
	x = float((raw_input("Enter no between 0 and 1")))
	for i in range(10):
		x = 3.9 * x * (1-x)
		print(x)


if __name__ == '__main__':
			main()		