def	find_start(x, y, lines):
	if x > 0:
		if lines[x - 1][y] == '|' or lines[x - 1][y] == 'L' or lines[x - 1][y] == 'J':
			return "up"
	if x < len(lines) - 1:
		if lines[x + 1][y] == '|' or lines[x + 1][y] == 'F' or lines[x + 1][y] == '7':
			return "down"
	if y > 0:
		if lines[x][y - 1] == '7' or lines[x][y - 1] == 'J' or lines[x][y - 1] == '-':
			return "right"
	if y < len(lines[x]) - 1:
		if lines[x][y + 1] == 'L' or lines[x][y + 1] == 'F' or lines[x][y + 1] == '-':
			return "left"
	return ""

file = open("ref", 'r')
lines = file.read().split('\n')
y = 0
x = 0
for z, line in enumerate(lines):
	if line.find('S') != -1:
		x = line.find('S')
		y = z
last_move = find_start(x, y, lines)
if last_move == "right":
	x +=1
elif last_move == "left":
	x -= 1
elif last_move == "up":
	y += 1
else:
	y -= 1
print(f"{y};{x} -> {last_move}")
rst = 1
while lines[y][x] != 'S':
	if lines[y][x] == '|':
		if last_move == "up":
			y -= 1
		else:
			y += 1			
	elif lines[y][x] == '-':
		if last_move == "right":
			x += 1
		else:
			x -= 1
	elif lines[y][x] == 'L':
		if last_move == "down":
			last_move = "right"
			x += 1
		else:
			last_move = "up"
			y -= 1
	elif lines[y][x] == 'J':
		if last_move == "down":
			last_move = "left"
			x -= 1
		else:
			last_move = "up"
			y -= 1
	elif lines[y][x] == '7':
		if last_move == "up":
			last_move = "left"
			x -= 1
		else:
			last_move = "down"
			y += 1
	elif lines[y][x] == 'F':
		if last_move == "up":
			last_move = "right"
			x += 1
		else:
			last_move = "down"
			y += 1
	rst += 1
print(rst)
print(rst / 2)