def	direction(lines, x, y, dir):
	if dir == "right":
		while x < len(lines[y]):
			if lines[y][x] != '.' and lines[y][x] != '#':
				break
			lines[y] = lines[y][:x] + '#' + lines[y][x + 1:]
			x += 1
	elif dir == "left":
		while x >= 0:
			if lines[y][x] != '.' and lines[y][x] != '#':
				break
			lines[y] = lines[y][:x] + '#' + lines[y][x + 1:]
			x -= 1
	elif dir == "up":
		while y >= 0:
			if lines[y][x] != '.' and lines[y][x] != '#':
				break
			lines[y] = lines[y][:x] + '#' + lines[y][x + 1:]
			y -= 1
	elif dir == "down":
		while y < len(lines):
			if lines[y][x] != '.' and lines[y][x] != '#':
				break
			lines[y] = lines[y][:x] + '#' + lines[y][x + 1:]
			y += 1
	return lines, x, y

def	rayon(lines, x, y, dir, tab):
	lines, x, y = direction(lines, x, y, dir)
	if x < 0 or x > len(lines[0]) - 1:
		return lines, tab
	if y < 0 or y > len(lines) - 1:
		return lines, tab
	char = lines[y][x]
	if char == '|':
		if [x, y, dir] not in tab:
			tab.append([x, y, dir])
			if dir == "left" or dir == "right":
				lines, tab = rayon(lines, x, y - 1, "up", tab)
				lines, tab = rayon(lines, x, y + 1, "down", tab)
			if dir == "up":
				lines, tab = rayon(lines, x, y - 1, "up", tab)
			if dir == "down":
				lines, tab = rayon(lines, x, y + 1, "down", tab)
	elif char == '-':
		if [x, y, dir] not in tab:
			tab.append([x, y, dir])
			if dir == "down" or dir == "up":
				lines, tab = rayon(lines, x + 1, y, "right", tab)
				lines, tab = rayon(lines, x - 1, y, "left", tab)
			if dir == "right":
				lines, tab = rayon(lines, x + 1, y, "right", tab)
			if dir == "left":
				lines, tab = rayon(lines, x - 1, y, "left", tab)
	elif char == '/':
		if [x, y, dir] not in tab:
			tab.append([x, y, dir])
			if dir == "right":
				lines, tab = rayon(lines, x, y - 1, "up", tab)
			elif dir == "left":
				lines, tab = rayon(lines, x, y + 1, "down", tab)
			elif dir == "up":
				lines, tab = rayon(lines, x + 1, y, "right", tab)
			elif dir == "down":
				lines, tab = rayon(lines, x - 1, y, "left", tab)
	elif char == '\\':
		if [x, y, dir] not in tab:
			tab.append([x, y, dir])
			if dir == "right":
				lines, tab = rayon(lines, x, y + 1, "down", tab)
			elif dir == "left":
				lines, tab = rayon(lines, x, y - 1, "up", tab)
			elif dir == "up":
				lines, tab = rayon(lines, x - 1, y, "left", tab)
			elif dir == "down":
				lines, tab = rayon(lines, x + 1, y, "right", tab)
	return lines, tab

def	copy(data):
	tab = []
	for line in data:
		string = ""
		for char in line:
			string += char
		tab.append(string)
	return tab

file = open("ref", 'r')
data = file.read().split('\n')
final = 0
for x in range(len(data[0])):
	y = 0
	lines = copy(data)
	tab = []
	lines, tab = rayon(lines, x, y + 1, "down", tab)
	rst = 0
	for value in tab:
		y = value[1]
		x = value[0]
		if lines[y][x] != '#':
			lines[y] = lines[y][:x] + '#' + lines[y][x + 1:]
	for line in lines:
		for char in line:
			if char == '#':
				rst += 1
	if final < rst:
		final = rst
for x in range(len(data[0])):
	y = len(data) - 1
	lines = copy(data)
	tab = []
	lines, tab = rayon(lines, x, y - 1, "up", tab)
	rst = 0
	for value in tab:
		y = value[1]
		x = value[0]
		if lines[y][x] != '#':
			lines[y] = lines[y][:x] + '#' + lines[y][x + 1:]
	for line in lines:
		for char in line:
			if char == '#':
				rst += 1
	if final < rst:
		final = rst
for y in range(len(data)):
	x = 0
	lines = copy(data)
	tab = []
	lines, tab = rayon(lines, x + 1, y, "right", tab)
	rst = 0
	for value in tab:
		y = value[1]
		x = value[0]
		if lines[y][x] != '#':
			lines[y] = lines[y][:x] + '#' + lines[y][x + 1:]
	for line in lines:
		for char in line:
			if char == '#':
				rst += 1
	if final < rst:
		final = rst
for y in range(len(data)):
	x = len(data[y])
	lines = copy(data)
	tab = []
	lines, tab = rayon(lines, x - 1, y, "left", tab)
	rst = 0
	for value in tab:
		y = value[1]
		x = value[0]
		if lines[y][x] != '#':
			lines[y] = lines[y][:x] + '#' + lines[y][x + 1:]
	for line in lines:
		for char in line:
			if char == '#':
				rst += 1
	if final < rst:
		final = rst
print(final)
# 7496