# ===  CODE IS WORKING  === #
 
# input_layer_size = 5 units
# hidden_layer_size = 4 units
# num_labels = 1 unit(ouput layer)
# m 

# Input, Hidden, Output, Iterations, Learning_rate.

# =================== numpy functions =======================
# k=np.array([1,2,3],dtype='float32')
# np.exp(l)
# np.arange(0,10,2)
# np.dot(d,e)  or  d.dot(e)  --> matrix multiplication of d and e.
# +,-,/,*                    --> Element-wise operation.
# a.shape
# np.zeros(shape=(x,y))
# np.random.randn(1,3)
# np.c_[ A, np.ones(N) ]     --> insert a column
# np.r_[ A, [A[1]] ]	     --> insert a row
# np.transpose(x)
# np.delete(a,0,1)           --> delete first column
# np.delete(a,1,0)           --> delete second column

import numpy as np

def sigmoid(z):
		return 1.0 / (1.0 + np.exp(-z))

def NeuralNetwork(object):
	  # Function to initialize
	  def __init__(self, x, hidden, ly, iterations, learningRate):

	  		  #            x : Number of units of hidden layer
		#       hidden : Number of units of hidden layer
		#            y : Number of units of output layer
		#   iterations : Number of iterations
		# learningRate : (for updating weights)
			  self.x = x
			  self.hidden = hidden
			  self.ly = ly
			  self.iterations = iterations
			  self.learningRate = learningRate
			  # Initialize weights randomly to avoid symmetry
			  self.m = 0

			  # self.theta1 : Weight between input layer and hidden layer
			  # self.theta2 : Weights between hidden layer and output layer
			  self.theta1 = np.random.randn(self.hidden, 1+self.x)
			  self.theta2 = np.random.randn(self.ly, 1+self.hidden)
			  self.h = np.zeros(shape=(y.shape[0],1))
			  self.y = np.zeros(shape=(y.shape[0],1))

	  # Train NN
	  def trainData(self, X, y):
	  		  self.m = X.shape[0]
	  		  for i in range(self.iterations):
	  		  		  		  		