def initialize(N, values, weights):
	things = [[values[i], weights[i]] for i in range(N)]
	things.sort(key=lambda x: x[0]/x[1])
	for i in range(N):
		values[i] = things[i][0]
		weights[i] = things[i][1]
	return

def solve(N, W, values, weights):
	initialize(N, values, weights)
	w_sum = 0
	for i in range(N):
		if w_sum+weights[i]<=W:
			w_sum += weights[i]
		else:
			pass


N, W = map(int, input().split())
values = [0 for i in range(N)]
weights = [0 for i in range(N)]
for i in range(N):
	values[i], weights[i] = map(int, input().split())

solve(N, W, values, weights)