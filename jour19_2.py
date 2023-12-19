file = open("ref", 'r')
lines = file.read().split('\n')
rules = [line for line in lines if line.find('=') == -1 and line != ""]
for x, rule in enumerate(rules):
	rules[x] = rule.split('{')
	rules[x][1] = rules[x][1].replace('}', '')
for rule in rules:
	print(rule)