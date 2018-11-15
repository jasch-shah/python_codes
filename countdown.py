import time
from datetime import datetime, timedelta

def setcount():
	global hrs
	global mins
	global secs
	global totalsecs
	print('#### enter the requested values of the countdown timer #')
	hrs = int(input('hrs: ' ))
	mins = int(input('minutes: '))
	secs = int(input('seconds: '))
	totalsecs = 3600 * hrs + 60 * mins + secs



def countdown():
	run = str(raw_input('Start? (y/n) >'))
	if run == "y":
		ltotalsecs = totalsecs
		while ltotalsecs != 0:
			sec = timedelta(seconds=int(ltotalsecs))
			d = datetime(1, 1, 1) + sec
			print("%d hr %d minutes %d seconds over"% (d.hour, d.minute, d.second))
			time.sleep(1)
			ltotalsecs -= 1
			if ltotalsecs == 0:
				print("Time is Up")

setcount()
countdown()