n = int(input())

for i in range(n):
	n,k = input().split('')
	n,k = [int(n),int(k)]
	print 2*(1+(k-1)/k)*(n-1)
