maxval = 1E10
def painter(arr,n,k):
	res = [[0 for _ in range(n)] for _ in range(k)]
	#when 1 painter
	sums = 0
	for i in range(n):
		sums += arr[i]
		res[0][i] = sums

	#when 1 board
	for i in range(k):
		res[i][0] = arr[0]

	for i in range(1,k):
		for j in range(1,n):
			temp = maxval
			for l in range(j):
				temp = min(temp,max(res[i-1][l],sum(arr[l+1:j+1])))
			res[i][j] = temp
	return res[k-1][n-1]

	t = int(raw_input())
	for i in range(t):
		k,n = list(map(int,raw_input().strip().split()))
		arr = list(map(int,raw_input().strip().split()))
		res = painter(arr,n,k)
		print res					