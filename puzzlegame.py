import sys
s_prime = {2,3,5,7,11,13,17}
dsr_state = (1,2,3,4,5,6,7,8,9)

all_states = {}
dist = 0

cur_states = {dsr_state:dist}

while cur_states:
	next_states = {}
	dist += 1