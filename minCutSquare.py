def solve(m,n):
	if m==n:
		return 1
	if (m,n) in dp:
		return dp[(m,n)]

	h_min = INT_MAX
	v_min = INT_MAX

	for i in range(1,int(m/2)+1):
		h_min = min(solve(i,n)+solve(m-i,n),h_min)

	for i in range(1,int(n/2)+1):
		v_min = min(solve(m,i)+solve(m,n-i),v_min)

	dp[(m,n)] = min(h_min,v_min)
	
	return dp[(m,n)]

INT_MAX = 999999
dp = dict()
tc = int(raw_input())
for count in range(tc):
	numbers = list(map(int,raw_input().split()))
	m = numbers[0]
	n = numbers[1]
	answer = solve(m,n)
	print answer			