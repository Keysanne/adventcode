def	all_g(lines):
	galaxy = []
	for y , line in enumerate(lines):
		for x , char in enumerate(line):
			if char == '#':
				galaxy.append([y, x])
	return galaxy

def	empty_lines(lines):
	empty_lines = []
	for y , line in enumerate(lines):
		for x , char in enumerate(line):
			if char == '#':
				break
			elif x == len(line) - 1:
				empty_lines.append(y)
	return empty_lines

def	empty_col(lines):
	empty_col = []
	for x in range(0, len(lines[0])):
		for y in range(0, len(lines)):
			if lines[y][x] == '#':
				break
			elif y == len(lines) - 1:
				empty_col.append(x)
	return empty_col

def	is_distorded(s, e, values):
	rst = 0
	for value in values:
		if value >= s and value <= e:
			rst += 1
	return rst

def	path(a, b, empty_l, empty_c):
	rst = 0
	distorsion = 1000000 - 1
	if a[0] > b[0]:
		rst += a[0] - b[0]
		rst += is_distorded(b[0], a[0], empty_l) * distorsion
	else:
		rst += b[0] - a[0]
		rst += is_distorded(a[0], b[0], empty_l) * distorsion
	if a[1] > b[1]:
		rst += a[1] - b[1]
		rst += is_distorded(b[1], a[1], empty_c) * distorsion
	else:
		rst += b[1] - a[1]
		rst += is_distorded(a[1], b[1], empty_c) * distorsion
	return rst

file = open("ref", 'r')
lines = file.read().split('\n')
galaxy = all_g(lines)
empty_l = empty_lines(lines)
empty_c = empty_col(lines)
rst = []
for x in range(0, len(galaxy)):
	for y in range(x + 1, len(galaxy)):
		rst.append(path(galaxy[x], galaxy[y], empty_l, empty_c))
print(sum(rst))