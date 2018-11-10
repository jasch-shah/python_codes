t = int(raw_input())
while(t):
	c = 0
	str1 = raw_input()
	str2 = raw_input()
	for i in range(len(str1)):
		if str1[i] !=  str2[i]:
			c = c+1
	if c==2:
		print '1'
	else:
		print '0'
	t=t+1				