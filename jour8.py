def	find_Z(where, route, g_d, rules):
	nb = 0
	while where[2] != 'Z':
		for char in rules:
			if where[2] == 'Z':
				break
			if char == 'R':
				where = g_d[route.index(where)][1]
			if char == 'L':
				where = g_d[route.index(where)][0]
			nb += 1
	return nb

def ppmc(rst, x):
	for value in rst:
		if x % value != 0:
			return 0
	return 1

file = open("ref", 'r')
lines = file.read().split('\n')
rules = lines.pop(0)
if lines[0] == "":
	lines.pop(0)
route = [y.split('=')[0].strip() for y in lines]
g_d = [y.split('=')[1].strip().replace('(', '').replace(')', '').replace(' ', '').split(',') for y in lines]
nb = 0
where = [y for y in route if y[2] == 'A']
rst = []
for value in where:
	rst.append(find_Z(value, route, g_d, rules))
intervalle = 1000000000
for x in range(intervalle, 10000000000):
	if ppmc(rst, x) == 1:
		print(x)
		break