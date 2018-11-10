import sys

n = int(sys.argv[1])

turn  = 1
first = 1
last = n

while n > 3:
	if n % 2 != 0: first += turn * 2
	else: last -= turn

	turn *= 2
	n = n //2

print(first,last)	

