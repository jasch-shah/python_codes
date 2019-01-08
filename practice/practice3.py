'''

Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

'''

def reverse(n):
	i = 0
	while i < n:
		j = i
		i = i+1
		if j % 7 == 0:
			yield j

for i in reverse(int(raw_input("enter n"))):
	print i			