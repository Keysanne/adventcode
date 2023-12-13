def	find_sym(tab):
	for x in range(0, len(tab) - 1):
		if tab[x] == tab[x + 1]: #check si un seul caractere different
			a = x - 1
			b = x + 2
			while a >= 0 and b < len(tab):
				if tab[a] != tab[b]:
					sym = -1
					break
				a -= 1
				b += 1
			if a < 0 or b >= len(tab):
				return x + 1
	return 0

def	change(tab):
	final = []
	for x in range(0, len(tab[0])):
		string = ""
		for y in range(0, len(tab)):
			string += tab[y][x]
		final.append(string)
	return final

file = open("ref", 'r')
lines = file.read().split('\n')
tab = []
rst_l = 0
rst_c = 0
for line in lines:
	if line == '':
		rst_l += find_sym(tab)
		rst_c += find_sym(change(tab))
		tab = []
	else:
		tab.append(line)
rst_l += find_sym(tab)
rst_c += find_sym(change(tab))
print(rst_c)
print(rst_l)
print(rst_c + (rst_l * 100))