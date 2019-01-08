'''
The numbers after the direction are steps. 
Please write a program to compute the distance from current position 
after a sequence of movement and original point. 
If the distance is a float,then just print the nearest integer.
'''
import math
pos = [0,0]

while True:
	s = raw_input()
	if not s:
		break
	movement = s.split(" ")
	direction = movement[0]
	steps = int(movement[1])
	if direction == "UP":
		pos[0] += steps
	elif direction == "DOWN":
		pos[0] -= steps
	elif direction == "LEFT":
		pos[1] -= steps
	elif direction == "RIGHT":
		pos[1] += steps
	else:
		pass

print int(round(math.sqrt(pos[1]**2 + pos[0]**2)))							