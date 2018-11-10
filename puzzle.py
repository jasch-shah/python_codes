import sys
s_prime = {2, 3, 5, 7, 11, 13, 17}
dsr_state = (1, 2, 3, 4, 5, 6, 7, 8, 9)
 
all_states = {}
dist = 0
cur_states = {dsr_state:dist}
 
while cur_states:
    next_states = {}
    dist += 1
    for state in cur_states:
        lstate = list(state)
        for i in range(2):
            for j in range(3):
                p1 = 3 * i + j
                p2 = p1 + 3
                if (state[p1] + state[p2]) in s_prime:
                    lstate[p1], lstate[p2] = lstate[p2], lstate[p1]
                    tstate = tuple(lstate)
                    if not tstate in all_states:
                        next_states[tstate] = dist
                    lstate[p1], lstate[p2] = lstate[p2], lstate[p1]
 
                p1 = 3 * j + i
                p2 = p1 + 1
                if (state[p1] + state[p2]) in s_prime:
                    lstate[p1], lstate[p2] = lstate[p2], lstate[p1]
                    tstate = tuple(lstate)
                    if not tstate in all_states:
                        next_states[tstate] = dist
                    lstate[p1], lstate[p2] = lstate[p2], lstate[p1]
 
        all_states[state] = cur_states[state]
    cur_states = next_states
            
T = int(sys.stdin.readline())
for i in range(T):
    sys.stdin.readline()
    in_state = []
    for j in range(3):
        in_state.extend(map(int, sys.stdin.readline().split()))
 
    in_state = tuple(in_state)
    print(all_states.get(in_state, -1))
  