def	update(rule, value):
	rule = rule.split(',')
	for line in rule:
		if line.find(':') != -1:
			line = line.split(':')
			key = "xmas"
			if line[0].find('<') != -1:
				for x, char in enumerate(key):
					if line[0][0] == char:
						if int(crt[x][2:]) < int(line[0][2:]):
							return line[1]
			elif line[0].find('>') != -1:
				for x, char in enumerate(key):
					if line[0][0] == char:
						if int(crt[x][2:]) > int(line[0][2:]):
							return line[1]
		else:
			return line

file = open("ref", 'r')
lines = file.read().split('\n')
rules = [line for line in lines if line.find('=') == -1 and line != ""]
values = [line for line in lines if line.find('=') != -1 and line != ""]
for x, rule in enumerate(rules):
	rules[x] = rule.split('{')
	rules[x][1] = rules[x][1].replace('}', '')
rst = 0
for value in values:
	go = "in"
	value = value.replace('{', '').replace('}', '')
	crt = value.split(',')
	while go != "R" and go != "A":
		rule = []
		for line in rules:
			if line[0] == go:
				rule = line
				break
		go = update(rule[1], crt)
	if go == 'A':
		for value in crt:
			x = int(value.split('=')[1]) 
			rst += x
print(rst)