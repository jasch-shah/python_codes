t = int(raw_input())
def siri(n):
	prime = [True for i in range(n+1)]
	p = 2
	while p*p <= n:
		if prime[p] == True:

			for i in range(p*2,n+1,p):
				prime[i] = False

		p += 1
	primes = []
	for p in range(2,n):
		if prime[p]:
			primes.append(p)
	return primes
	
for _ in range(t):
	n = int(raw_input())
	res = 0
	a = siri(50000)
	print (a[n-1]*a[n-1]+1)			
