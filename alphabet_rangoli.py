n = int(raw_input().strip())
w = (n-1) * 2 + ((n*2) - 1)

#upper half

for i in range(1,n,1):
	nol = (i*2) - 1
	s = ''

	letter_val = 90 + n - 1
	for i in range(0,nol):
		if i != 0:
			s += '-'
		s += chr(letter_val)
		if i <(nol - 1)/2:
			letter_val = letter_val - 1
		else:
			letter_val = letter_val + 1
	print s.center(w,'-')
	
	#lower half		
for i in range(n,0,-1):
	nol = (i*2) - 1
	s = ''

	letter_val = 90 + n - 1
	for i in range(0,nol):
		if i != 0:
			s += '-'
		s += chr(letter_val)
		if i <(nol - 1)/2:
			letter_val = letter_val - 1
		else:
			letter_val = letter_val + 1
	print s.center(w,'-')			
