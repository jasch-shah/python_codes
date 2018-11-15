import time

def countdown(count):
	while(count >= 0):
		print('The count is: ', count)
		count -= 1
		time.sleep(1)

countdown(10)
print('Good Bye..')		
