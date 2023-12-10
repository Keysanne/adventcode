file = open("ref", 'r')
lines = file.read().split('\n')
rules = lines.pop(0)
if lines[0] == "":
	lines.pop(0)
route = [y.split('=')[0].strip() for y in lines]
g_d = [y.split('=')[1].strip().replace('(', '').replace(')', '').replace(' ', '').split(',') for y in lines]
nb = 0
where = "AAA"
while where != "ZZZ":
	for char in rules:
		if where == "ZZZ":
			break
		if char == 'R':
			where = g_d[route.index(where)][1]
			nb += 1
		if char == 'L':
			where = g_d[route.index(where)][0]
			nb += 1
print(f"{where} en {nb} coups")