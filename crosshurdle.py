for test in range(0,int(raw_input())):
	si = int(raw_input())
	ene = list(map(int,raw_input().split()))
	hud = list(map(int,raw_input().split()))
	t = 0
	co = 0

	for i in range(0,si):
		t = t + ene[i]
		#print t

		if t >= hud[i]:
			t = t-hud[i]
			t = t+i+1
		else:
			co = 1

	if co==1:
	   print "Game Over"
	else:
		print "You Win "+str(t)

			
		
