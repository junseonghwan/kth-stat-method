from q2generator import *
import numpy as np
import pdb

def conditional_likelihood(G, start):
	pass

# o: observations
# n_lattice: size of the lattice
# num_iter: number of MCMC iterations
def mh_w_gibbs(o, n_lattice, num_iter):
	G = initialize_graph(n_lattice)
	s = [] # store samples for the start positions
	X = [] # store switch states
	X.append(G) # initial sample
	s.append(G[0][0]) # set the initial start position as the one at G[0][0]
	for n in range(num_iter):
		pass
	return s, X

def gibbs(o, n_lattice, num_iter):
	G = initialize_graph(n_lattice)
	s = [] # store samples for the start positions
	X = [] # store switch states
	X.append(G) # initial sample
	s.append(G[0][0]) # set the initial start position as the one at G[0][0]
	for n in range(num_iter):

		pass
	return s, X

def block_gibbs(o, n_lattice, num_iter):
	G = initialize_graph(n_lattice)
	s = [] # store samples for the start positions
	X = [] # store switch states
	X.append(G) # initial sample
	s.append(G[0][0]) # set the initial start position as the one at G[0][0]
	for n in range(num_iter):
		pass
	return s, X

# generate sample graph and observations
def main():
	seed = 2
	n_lattice = 3
	T = 100
	p = 0.1
	G_truth, s_truth, o = generate_data(seed, T, n_lattice, p)
	print(o)
	print(s_truth)

	# discard G and s 
	# infer s[0] and switch states given o
	num_iter = 1000
	s, X = mh_w_gibbs(o, n_lattice, num_iter)
	s, X = gibbs(o, n_lattice, num_iter)
	s, X = block_gibbs(o, n_lattice, num_iter)
	
	# YOUR CODE:
	# analyze s, X by comparinson to the ground truth in s[0] and G
	# check for convergence

if __name__ == '__main__':
	main()