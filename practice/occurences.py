def countOccurences(arr, n, x):
	res = 0
	for i in range(n):
		if x == arr[i]:
			res += 1
	return res


arr = list()
n = raw_input("Enter n")
arr.append(int(n))
x = raw_input("Enter x")
print(countOccurences(arr, n, x))