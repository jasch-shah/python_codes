import numpy as np 
import time

#variables

n_hidden = 10
n_in = 10
#outputs
n_out = 10
n_sample = 300

#hyper params
learning_rate = 0.01
momentum = 0.9	#lower the loss function

#non deterministic seeding
np.random.seed(0)	#while testing the numbers we want same random nos to be generated when every time we run the code.Seeding generates same random nos each time we execute the code

def sigmoid(x):
	return 1.0/(1.0 + np.exp(-x))


#sigmoid function turns number into probabilities.Well in our neural network
#when we have our input data it goes through the network and each of the weight is a set
#of probabilities like which way shoulg I go..And these probabilities are updated when we train our neural networks
#so its gets better and better over time
#here the sigmoid fn is our activation function...


#In these XOR problem we are going to use two activation function
#1->Sigmoid Function
#2->Tangent Function. ..It's makes the loss function more efficient

#second layer activation function
def tanh_prime(x):
	return 1 - np.tanh(x)**2




def train(x, t, V, W, bv, bw):
	'''
	x is our input data
	t is our tanspose for matrix multipication
	V and W are our layers
	bv and bw are the biases..Biases gonna help us to make more accurate predictions
	one bias for each layer

	'''
	#forward--> matrix multiply + bias

	A = np.dot(x, V) + bv 	#dot product of dataset
	Z = np.tanh(A)		

	B = np.dot(Z, W) + bw
	Y = sigmoid(B)


	#backward
	Ew = Y- t 
	Ev = tanh_prime(A) * np.dot(W, Ew)

	#predict loss

	dW = np.outer(Z, Ew)
	dV = np.outer(x, Ev)

	#cross entropy->bcoz we are doing classification 
	loss = -np.mean(t * np.log(Y) + (1 - t) * np.log(1 - Y))

	return loss, (dV, dW, Ev, Ew)

def predict(x, V, W, bv, bw):
		A = np.dot(x, V)  + bv
		B = np.dot(np.tanh(A), W) + bw
		return (sigmoid(B) > 0.5).astype(int)


#create layers

V = np.random.normal(scale=0.1, size=(n_in, n_hidden))
W = np.random.normal(scale=0.1, size=(n_hidden, n_out))


bv = np.zeros(n_hidden)
bw = np.zeros(n_out)


params = [ V, W, bv, bw]

#generate our data
X = np.random.binomial(1, 0.5, (n_sample, n_in))
T = X ^ 1

#training time

for epoch in range(100):
	err = []
	upd = [0]*len(params)

	t0 = time.clock()
	#for each data point ,update weights of our network
	for i in range(X.shape[0]):
		loss,grad = train(X[i], T[i], *params)
		#update loss
		for j in range(len(params)):
			params[j] -= upd[j]

		for j in range(len(params)):
			upd[j] = learning_rate * grad[j] + momentum * upd[j]

		err.append(loss)
		
	print('Epoch : %d, Loss: %.8f, Time: %4fs' %(
	epoch, np.mean(err), time.clock()-t0))


	#now predict something
	x = np.random.binomial(1, 0.5, n_in)
	print('XOR prediction')
	print(x)
	print(predict(x, *params))		






