cartes = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

def	J(line, j):
	global cartes
	value = 0
	for y in cartes:
		x = 0
		for z in line:
			if z == "J":
				continue
			if z == y:
				x += 1
		if x == 2 and value == 2:
			value = 5
		if x > value:
			value = x
	print(value)
	print(j)
	if j == 5:
		return 7
	if j == 4:
		return 7
	if j == 3:
		if value == 2:
			return 7
		else:
			return 6
	if j == 2:
		if value == 3:
			return 7
		if value == 2:
			return 6
		else:
			return 4
	if j == 1:
		if value == 4:
			return 7
		if value == 3:
			return 6
		if value == 2:
			return 4
		if value == 5:
			return 5
		else:
			return 2

def find_value(line):
	global cartes
	value = 0
	j = 0
	for i in line:
		if i == "J":
			j += 1
	if j != 0:
		return J(line, j)
	for y in cartes:
		x = 0
		for z in line:
			if z == "J":
				continue
			if z == y:
				x += 1
		if x == 5 or x == 4:
			x+= 2
		elif (value == 4 and x == 2) or (value == 2 and x == 3):
			x = 5
		elif x == 3:
			x = 4
		elif value == 2 and x == 2:
			x = 3
		if x > value:
			value = x
	return value

def	combinaison(old, new):
	global cartes
	ov = find_value(old)
	nv = find_value(new)
	if ov == nv:
		for x in range(0 , len(old)):
			ov += cartes.index(old[x])
			nv += cartes.index(new[x])
			if ov != nv:
				break
	if ov > nv:
		return 1
	return 0

file = open("ref", 'r')
lines = file.read().split('\n')
rst = []
for x, line in enumerate(lines):
	z = 0
	if x == 0:
		rst.append(line.split(' '))
	else:
		for y, tab in enumerate(rst):
			if combinaison(tab[0], line.split(' ')[0]) == 1:
				rst.insert(y, line.split(' '))
				z = 1
			if z == 1:
				break
		if z == 0:
			rst.append(line.split(' '))
for x, line in enumerate(rst):
	print(f"{line[0]} -> {find_value(line[0])}")
	rst[x] = (x + 1) * int(rst[x][1])
print(sum(rst))

