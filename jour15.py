def	hash_algorithm(value):	
	rst = 0
	for char in value:
		if char == '=' or char == '-':
			break
		rst += ord(char)
		rst *=  17
		rst %= 256
	return rst

file = open("ref", 'r')
lines = file.read().split(',')
final = 0
tab = []
for value in lines:
	if value.find('=') > 0:
		for x, y in enumerate(tab):
			if value.split('=')[0] in y:
				tab[x] = [hash_algorithm(value), value.split('=')[0], value.split('=')[1]]
				continue
		if [hash_algorithm(value), value.split('=')[0], value.split('=')[1]] not in tab:
			tab.append([hash_algorithm(value), value.split('=')[0], value.split('=')[1]])
	else:
		for x, y in enumerate(tab):
			if value.split('-')[0] in y:
				del(tab[x])
final = 0
for x in range(0, 256):
	y = 0
	for value in tab:
		if x == value[0]:
			final += (value[0] + 1) * (y + 1) * int(value[2])
			y += 1
print(final)