import numpy as np
import pdb

def validate_idx(row, col, n):
	r = row
	c = col
	if row < 0:
		r = n-1
	elif row >= n:
		r = 0
	if col < 0:
		c = n-1
	elif col >= n:
		c = 0
	return (r, c)

class Switch:
	n = 0
	def __init__(self, row, col, state):
		self.row = row
		self.col = col
		self.state = state
		self.sample_edge_labels()

	def sample_edge_labels(self):
		self.edges = [(-1, 0), (0, -1), (1, 0), (0, 1)]
		np.random.shuffle(self.edges)

	def equals_0_dir(self, e):
		(i, j) = self.get_0_dir()
		if i == e.row and j == e.col:
			return True
		return False

	def get_0_dir(self):
		i, j = self.edges[0]
		return validate_idx(self.row + i, self.col + j, Switch.n)

	def __repr__(self):
		ret = "\npos: " + str(self.row) + ", " + str(self.col) + "\n"
		ret += "state: " + str(self.state) + "\n"
		for i in range(len(self.edges)):
			ret += str(i) + ": " + str(self.edges[i]) + "\n"
		return ret

# generate graph and switch states
# n >= 2
def initialize_graph(n = 2):
	X = []
	for i in range(n):
		row = []
		for j in range(n):
			state = np.random.randint(low=1, high=4, size=1)[0]
			row.append(Switch(i, j, state))
		X.append(row)
	return X

def generate_single_obs(prev, curr, p):
	true_state = curr.state
	u = np.random.uniform(0, 1, 1)[0]
	if u < p:
		#print("return random state")
		return np.random.randint(0, 4, 1)[0]
	#print("return true state")
	if prev == None or curr.equals_0_dir(prev):
		return true_state
	else:
		return 0

def advance_train(prev, curr, p):
	if prev is None or curr.equals_0_dir(prev):
		(i, j) =  curr.edges[curr.state]
		(row, col) =  validate_idx(curr.row + i, curr.col + j, Switch.n)
	else:
		(row, col) =  curr.get_0_dir()
	return row, col

# sample starting position
def simulate(X, T, p):
	n = len(X)
	row = np.random.randint(0, n, 1)[0]
	col = np.random.randint(0, n, 1)[0]
	s = []
	o = []

	prev = None
	curr = X[row][col]
	s.append(curr)
	o.append(generate_single_obs(prev, curr, p))
	#print("t: ", 0, "\nobs: " + str(o[0]), "\ncurr[", s[0], "]\n")
	for t in range(1, T):
		row, col = advance_train(prev, curr, p)
		prev = curr
		curr = X[row][col]
		obs = generate_single_obs(prev, curr, p)
		s.append(curr)
		o.append(obs)
		#print("t: ", (t), "\nobs: " + str(o[t]), "\ncurr[", s[t], "]\n")
	return s, o

def generate_data(seed, T, n, p):
	np.random.seed(seed)
	Switch.n = n
	X = initialize_graph(n)
	s, o = simulate(X, T, p)
	return X, s, o
