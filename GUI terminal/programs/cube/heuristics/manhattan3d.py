import math

def cubeManhattan3dHeuristic(state):
	c_sum = 0
	e_sum = 0

	u = state[1][0][1].sides["U"]
	f = state[1][1][2].sides["F"]
	r = state[2][1][1].sides["R"]
	d = state[1][2][1].sides["D"]
	b = state[1][1][0].sides["B"]
	l = state[0][1][1].sides["L"]

	c_i = state[0][0][0].sides["U"]
	c_j = state[0][0][0].sides["B"]
	c_k = state[0][0][0].sides["L"]
	if c_i != u and c_j != b and c_k != l:
		c_sum += 2
	elif c_i == u and c_j != b and c_k != l:
		c_sum += 1
	elif c_i != u and c_j == b and c_k != l:
		c_sum += 1
	elif c_i != u and c_j != b and c_k == l:
		c_sum += 1

	c_i = state[0][0][2].sides["U"]
	c_j = state[0][0][2].sides["F"]
	c_k = state[0][0][2].sides["L"]
	if c_i != u and c_j != f and c_k != l:
		c_sum += 2
	elif c_i == u and c_j != f and c_k != l:
		c_sum += 1
	elif c_i != u and c_j == f and c_k != l:
		c_sum += 1
	elif c_i != u and c_j != f and c_k == l:
		c_sum += 1

	c_i = state[0][2][0].sides["D"]
	c_j = state[0][2][0].sides["B"]
	c_k = state[0][2][0].sides["L"]
	if c_i != d and c_j != b and c_k != l:
		c_sum += 2
	elif c_i == d and c_j != b and c_k != l:
		c_sum += 1
	elif c_i != d and c_j == b and c_k != l:
		c_sum += 1
	elif c_i != d and c_j != b and c_k == l:
		c_sum += 1

	c_i = state[0][2][2].sides["F"]
	c_j = state[0][2][2].sides["D"]
	c_k = state[0][2][2].sides["L"]
	if c_i != f and c_j != d and c_k != l:
		c_sum += 2
	elif c_i == f and c_j != d and c_k != l:
		c_sum += 1
	elif c_i != f and c_j == d and c_k != d:
		c_sum += 1
	elif c_i != f and c_j != d and c_k == l:
		c_sum += 1

	c_i = state[2][0][0].sides["U"]
	c_j = state[2][0][0].sides["R"]
	c_k = state[2][0][0].sides["B"]
	if c_i != u and c_j != r and c_k != b:
		c_sum += 2
	elif c_i == u and c_j != r and c_k != b:
		c_sum += 1
	elif c_i != u and c_j == r and c_k != b:
		c_sum += 1
	elif c_i != u and c_j != r and c_k == b:
		c_sum += 1

	c_i = state[2][0][2].sides["U"]
	c_j = state[2][0][2].sides["F"]
	c_k = state[2][0][2].sides["R"]
	if c_i != u and c_j != f and c_k != r:
		c_sum += 2
	elif c_i == u and c_j != f and c_k != r:
		c_sum += 1
	elif c_i != u and c_j == f and c_k != r:
		c_sum += 1
	elif c_i != u and c_j != f and c_k == r:
		c_sum += 1

	c_i = state[2][2][0].sides["R"]
	c_j = state[2][2][0].sides["D"]
	c_k = state[2][2][0].sides["B"]
	if c_i != r and c_j != d and c_k != b:
		c_sum += 2
	elif c_i == r and c_j != d and c_k != b:
		c_sum += 1
	elif c_i != r and c_j == d and c_k != b:
		c_sum += 1
	elif c_i != r and c_j != d and c_k == b:
		c_sum += 1

	c_i = state[2][2][2].sides["F"]
	c_j = state[2][2][2].sides["R"]
	c_k = state[2][2][2].sides["D"]
	if c_i != f and c_j != r and c_k != d:
		c_sum += 2
	elif c_i == f and c_j != r and c_k != d:
		c_sum += 1
	elif c_i != f and c_j == r and c_k != d:
		c_sum += 1
	elif c_i != f and c_j != r and c_k == d:
		c_sum += 1

	e_i = state[0][0][1].sides["U"]
	e_j = state[0][0][1].sides["L"]
	if e_i == l or e_j == u:
		e_sum += 3
	elif e_i != u and e_j != l:
		e_sum += 2
	elif e_i == u and e_j != l:
		e_sum += 1
	elif e_i != u and e_j == l:
		e_sum += 1

	e_i = state[0][1][0].sides["B"]
	e_j = state[0][1][0].sides["L"]
	if e_i == l or e_j == b:
		e_sum += 3
	elif e_i != b and e_j != l:
		e_sum += 2
	elif e_i == b and e_j != l:
		e_sum += 1
	elif e_i != b and e_j == l:
		e_sum += 1

	e_i = state[0][1][2].sides["F"]
	e_j = state[0][1][2].sides["L"]
	if e_i == l or e_j == f:
		e_sum += 3
	elif e_i != f and e_j != l:
		e_sum += 2
	elif e_i == f and e_j != l:
		e_sum += 1
	elif e_i != f and e_j == l:
		e_sum += 1

	e_i = state[0][2][1].sides["D"]
	e_j = state[0][2][1].sides["L"]
	if e_i == l or e_j == d:
		e_sum += 3
	elif e_i != d and e_j != l:
		e_sum += 2
	elif e_i == d and e_j != l:
		e_sum += 1
	elif e_i != d and e_j == l:
		e_sum += 1

	e_i = state[1][0][0].sides["U"]
	e_j = state[1][0][0].sides["B"]
	if e_i == b or e_j == u:
		e_sum += 3
	elif e_i != u and e_j != b:
		e_sum += 2
	elif e_i == u and e_j != b:
		e_sum += 1
	elif e_i != u and e_j == b:
		e_sum += 1

	e_i = state[1][0][2].sides["U"]
	e_j = state[1][0][2].sides["F"]
	if e_i == f or e_j == u:
		e_sum += 3
	elif e_i != u and e_j != f:
		e_sum += 2
	elif e_i == u and e_j != f:
		e_sum += 1
	elif e_i != u and e_j == f:
		e_sum += 1

	e_i = state[1][2][0].sides["D"]
	e_j = state[1][2][0].sides["B"]
	if e_i == b or e_j == d:
		e_sum += 3
	elif e_i != d and e_j != b:
		e_sum += 2
	elif e_i == d and e_j != b:
		e_sum += 1
	elif e_i != d and e_j == b:
		e_sum += 1

	e_i = state[1][2][2].sides["F"]
	e_j = state[1][2][2].sides["D"]
	if e_i == d or e_j == f:
		e_sum += 3
	elif e_i != f and e_j != d:
		e_sum += 2
	elif e_i == f and e_j != d:
		e_sum += 1
	elif e_i != f and e_j == d:
		e_sum += 1

	e_i = state[2][0][1].sides["U"]
	e_j = state[2][0][1].sides["R"]
	if e_i == r or e_j == u:
		e_sum += 3
	elif e_i != u and e_j != r:
		e_sum += 2
	elif e_i == u and e_j != r:
		e_sum += 1
	elif e_i != u and e_j == r:
		e_sum += 1

	e_i = state[2][1][0].sides["R"]
	e_j = state[2][1][0].sides["B"]
	if e_i == b or e_j == r:
		e_sum += 3
	elif e_i != r and e_j != b:
		e_sum += 2
	elif e_i == r and e_j != b:
		e_sum += 1
	elif e_i != r and e_j == b:
		e_sum += 1

	e_i = state[2][1][2].sides["F"]
	e_j = state[2][1][2].sides["R"]
	if e_i == r or e_j == f:
		e_sum += 3
	elif e_i != f and e_j != r:
		e_sum += 2
	elif e_i == f and e_j != r:
		e_sum += 1
	elif e_i != f and e_j == r:
		e_sum += 1

	e_i = state[2][2][1].sides["R"]
	e_j = state[2][2][1].sides["D"]
	if e_i == d or e_j == r:
		e_sum += 3
	elif e_i != r and e_j != d:
		e_sum += 2
	elif e_i == r and e_j != d:
		e_sum += 1
	elif e_i != r and e_j == d:
		e_sum += 1
	
	return math.ceil(max(c_sum / 4, e_sum / 4))