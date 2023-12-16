def	roule_nord(lines):
	for x in range(len(lines[0])):
		for y in range(len(lines)):
			if lines[y][x] == '.':
				new = y
				while new < len(lines) - 1:
					if lines[new][x] != '.':
						break
					new += 1
				if lines[new][x] == 'O':
					lines[new] = lines[new][:x] + '.' + lines[new][x + 1:]
					lines[y] = lines[y][:x] + 'O' + lines[y][x + 1:]
	return lines

def	roule_sud(lines):
	for x in range(len(lines[0])):
		for y in range(len(lines))[::-1]:
			if lines[y][x] == '.':
				new = y
				while new > 0:
					if lines[new][x] != '.':
						break
					new -= 1
				if lines[new][x] == 'O':
					lines[new] = lines[new][:x] + '.' + lines[new][x + 1:]
					lines[y] = lines[y][:x] + 'O' + lines[y][x + 1:]
	return lines

def	roule_ouest(lines):
	for y in range(len(lines)):
		for x in range(len(lines[0])):
			if lines[y][x] == '.':
				new = x
				while new < len(lines) - 1:
					if lines[y][new] != '.':
						break
					new += 1
				if lines[y][new] == 'O':
					lines[y] = lines[y][:x] + 'O' + lines[y][x + 1:]
					lines[y] = lines[y][:new] + '.' + lines[y][new + 1:]
	return lines

def	roule_est(lines):
	for y in range(len(lines)):
		for x in range(len(lines[0]))[::-1]:
			if lines[y][x] == '.':
				new = x
				while new > 0:
					if lines[y][new] != '.':
						break
					new -= 1
				if lines[y][new] == 'O':
					lines[y] = lines[y][:x] + 'O' + lines[y][x + 1:]
					lines[y] = lines[y][:new] + '.' + lines[y][new + 1:]
	return lines

def	copie(lines):
	map = []
	for line in lines:
		string = ""
		for char in line:
			string += char
		map.append(string)
	return map

file = open("ref", 'r')
lines = file.read().split('\n')
cycle = []
taille = 0
entree = 0
x = 1
while x <= 1000000000:
	lines = roule_nord(lines)
	lines = roule_ouest(lines)
	lines = roule_sud(lines)
	lines = roule_est(lines)
	if lines not in cycle:
		cycle.append(copie(lines))
	else:
		for j, i in enumerate(cycle):
			if lines == i:
				entree = j + 1
		x = (1000000000 - ((1000000000 - entree) % (x - entree))) + 1
		while (x <= 1000000000):
			lines = roule_nord(lines)
			lines = roule_ouest(lines)
			lines = roule_sud(lines)
			lines = roule_est(lines)
			x += 1
	x += 1
final = 0
for y, line in enumerate(lines):
	for char in line:
		if char == 'O':
			final += len(lines) - y
print(final)