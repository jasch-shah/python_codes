'''
from heapq import *

m,n = list(map(int,raw_input().split()))
arr = list(map(int,raw_input().split()))
h = []
for i in arr:
	heappush(h,-i)
ans = 0
while n>0:
	val = -heappop(h)
	m -= 1
	if val <= n:
		n -= val
		ans += 1+val *(val+1)//2
	else:
		ans = 1+n *(n+1)//2
		break
print ans+m		
'''

n,m = map(int,raw_input().split())
pizza = map(int,raw_input().split())
maxCut = 0
slashed = 0
for cut in sorted(pizza,reverse=True):
  if cut>m:
  	maxCut += (m**2+m+2)/2
  	slashed += 1
  	break
  else:
  	maxCut += (cut**2+cut+2)/2
  	m -= cut
  	slashed += 1
print maxCut+n-slashed  	 	

		
