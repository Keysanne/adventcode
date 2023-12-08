cartes = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def	combinaison(line):


file = open("ref", 'r')
lines = file.read().split('\n')
rst = []
for x, line in enumerate(lines):
	if x == 0:
		rst.append(line.split(' '))
	else:
		for y, tab in enumerate(rst):
			if y == len(rst) - 1:
				rst.append(line.split(' '))
				break
			else:
				if combinaison(tab) > combinaison(line):
					rst.insert(line.split(' '))
print(rst)