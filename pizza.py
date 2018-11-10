from heapq import heappush,heappop
t = int(raw_input())
for i in range(t):
	n = int(raw_input())
	arr = []
	for j in range(n):
		a,b = map(int,raw_input().split())
		heappush(arr,(a+b,j+1))


	while arr:
		val = heappop(arr)[1]
		print val	