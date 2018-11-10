''' Discount Factor '''
gamma = 1
'''Probability of home team winning '''
p = 0.4
# no of states
numStates = 100
# list for storing the reward value
reward = [0 for _ in range(101)]
reward[100] = 1
# small threshold value
theta = 0.00000001

value = [0 for _ in range(101)]
policy = [0 for _ in range(101)]

def reinforcement_learning():
	delta = 1
	while delta > theta:
		delta = 0
		for i in range(1, numStates):
			oldvalue = value[i]
			bellmanequation(i)
			diff = abs(oldvalue-value[i])
			delta = max(delta, diff)
	print(value)

def bellmanequation(num):
	optimalvalue = 0

	for bet in range(0, min(num,100-num)+1):
		win = num+bet
		loss = num - bet

		sum = p * (reward[win] + gamma * value[win]) + (1-p) * (reward[loss] + gamma * value[loss])
		if sum > optimalvalue:
			optimalvalue = sum
			value[num] = sum
			policy[num] = bet

reinforcement_learning()						