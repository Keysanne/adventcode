def	set_up(dir, nbr, size):
	tab = []
	for y in range(size + 1):
		tab.append([])
	return tab

def	start(dir, nbr):
	where = 0
	final = []
	for x in range(len(dir)):
		if dir[x] == 'U':
			where -= nbr[x]
		elif dir[x] == 'D':
			where += nbr[x]
		final.append(where)
	return abs(min(final)), max(final) + abs(min(final))


file = open("ref", 'r')
lines = file.read().split('\n')
dir = []
nbr = []
for line in lines:
	dir.append(line.split(' ')[0])
	nbr.append(int(line.split(' ')[1]))
x = 0
y = 0
y, size = start(dir, nbr)
tab = set_up(dir, nbr, size)
for i in range(len(dir)):
	if dir[i] == 'R':
		for z in range(nbr[i]):
			x += 1
			tab[y].append(x)
	if dir[i] == 'L':
		for z in range(nbr[i]):
			x -= 1
			tab[y].append(x)
	if dir[i] == 'U':
		for z in range(nbr[i]):
			y -= 1
			tab[y].append(x)
	if dir[i] == 'D':
		for z in range(nbr[i]):
			y += 1
			tab[y].append(x)
final = []
mini = 0
maxi = 0
for line in tab:
	if line != []:
		if mini > min(line):
			mini = min(line)
		if maxi < max(line):
			maxi = max(line)
maxi += abs(mini) + 1
for line in tab:
	string = ""
	x = 0
	while x in range(maxi):
		if x + mini in line:
			string += '#'
			x += 1
		else:
			string += '.'
			x += 1
	final.append(string)
# add a floodfill
rst = 0
for line in final:
	print(line)
	for char in line:
		if char == '#':
			rst += 1
print(rst)