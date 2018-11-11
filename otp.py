from random import *
ch = 'y'
while ch == 'y':
	m = int(input('Enter your number'))
	n = str(randint(1000,2000))
	f = open('newFile.txt','w')
	f.write(n)
	f.close()
	f=open('newFile.txt','r')
	data=f.read()
	print('Your OTP has been sended to newFile.txt')
	OTP=int(input('Enter the OTP:'))
	if(data==n):
		print('Payment Successful')
	else:
		print('Try Again')
	ch = input("Do u want to do more conversions ?? y//n: ")

print('Thank You !!!')
f.close()			