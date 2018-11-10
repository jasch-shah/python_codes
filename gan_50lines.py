import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

# Data params
data_mean = 4
data_stddev = 1.25

# Model params

g_input_size = 1
g_hidden_size = 50
g_output_size = 1
d_input_size = 100
d_hidden_size = 50
d_output_size = 1
minibatch = d_input_size

d_learning_rate = 2e-4
g_learning_rate = 2e-4
optim_betas = (0.9, 0.999)
num_epochs = 30000
print_interval = 200
d_steps = 1
g_steps = 1

(name, preprocess, d_input_func) = ("Data and Vairances", lambda data: decorate_with_diffs(data, 2.0), lambda x: x*2)

print("Using data [%s]" % (name))

def get_distrubution_sampler(mu, sigma):
	return lambda n: torch.Tensor(np.random.normal(mu, sigma, (1,n)))

def get_generator_input_sampler():
	return lambda m, n:torch.rand(m, n)


# Generator Model
class Generator(nn.Module):
	def __init__(self, input_size, hidden_size, output_size):
		super(Generator, self).__init__()
		self.map1 = nn.Linear(input_size, hidden_size)
		self.map2 = nn.Linear(hidden_size, hidden_size)
		self.map3 = nn.Linear(hidden_size, output_size)


	def forward(self, x):
		x = F.elu(self.map1(x))	
		x = F.sigmoid(self.map2(x))
		return self.map3(x)



class Discriminator(nn.Module):
	def __init__(self, input_size, hidden_size, output_size):
		super(Discriminator, self).__init__()
		self.map1 = nn.Linear(input_size, hidden_size)
		self.map2 = nn.Linear(hidden_size, hidden_size)
		self.map3 = nn.Linear(hidden_size, output_size)

	def forward(self, x):
		x = F.elu(self.map1(x))
		x = F.elu(self.map2(x))
		return F.sigmoid(self.map3(x))


	def extract(v):
		return v.data.storage().toList()

	def stats(d):
		return [np.mean(d), np.std(d)]

	def decorate_with_diffs(data, exponent):
		mean = torch.mean(data.data, 1, keepdim = True)
		mean_broadcast = torch.mul(torch.ones(dat.size()), mean.toList()[0][0])	
		diffs = torch.pow(data - Variable(mean_broadcast), exponent)
		return torch.cat([data, diffs], 1)

	d_sampler = get_distrubution_sampler(data_mean, data_stddev)
	gi_sampler = get_generator_input_sampler()
	G = Generator(input_size=g_input_size, hidden_size=g_hidden_size, output_size=g_output_size)
	D = Discriminator(input_size=d_input_size, hidden_size=d_hidden_size, output_size=d_output_size)
	criterion = nn.BCELoss()	#Binary Cross Entropy
	d_optimizer = optim.Adam(D.parameters(), lr=d_learning_rate, betas=optim_betas)
	g_optimizer = optim.Adam(D.parameters(), lr=g_learning_rate, betas=optim_betas)


	for epoch in range(num_epochs):
		for d_index in range(d_steps):
			# 1.Train D on real + fake
			D.zero_grad()

			# 1A:Train D on real
			d_real_data = Variable(d_sampler(d_input_size))
			d_real_decision = D(preprocess(d_real_data))
			d_real_error = criterion(d_real_decision, Variable(torch.one(1)))	# 1->True
			d_real_error.backward()	# compute/store gradients but don't change params

			# 1B:Train D on fake
			d_gen_input = Variable(gi_sampler(minibatch_size, g_input_size))
			d_fake_data = G(d_gen_input).detach()
			d_fake_decision = D(preprocess(d_fake_data.t()))
			d_fake_error = criterion(d_fake_decision, Variable(torch.zeros(1)))	# zeros = fake
			d_optimizer.step()	# only optimize D's parameters  changes based on  stored gradients from backward()


		for g_index in range(g_steps):
			# 2: Train G & D's response (but don not train D on these labels)
			G.zero_grad()


			gen_input = Variable(gi_sampler(minibatch_size, g_input_size ))
			g_fake_data = G(gen_input)
			dg_fake_decision = D(preprocess(g_fake_data.t()))
			g_error = criterion(dg_fake_decision, Variable(torch.ones(1))) #we want to fool,so be genuine

			g_error.backward()
			g_optimizer.step()

		if epoch % print_interval == 0:
			print("%s: D: %s/%s G: %s (Real: %s, Fake: %s)" % (epoch,
															   extract(d_real_error)[0],
															   extract(d_fake_error)[0],
															   extract(g_error)[0],
															   stats(extract(d_real_data)),
															   stats(extract(d_fake_data)))		


