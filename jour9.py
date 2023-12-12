def	all_zero(line):
	for x in line:
		if x != 0:
			return 0
	return 1

def	next(line):
	suite = []
	suite.append([int(x) for x in line.split(' ')])
	while all_zero(suite[len(suite) - 1]) == 0:
		new = []
		for x, value in enumerate(suite[len(suite) - 1]):
			if x < len(suite[len(suite) - 1]) - 1:
				new.append(suite[len(suite) - 1][x + 1] - value)
		suite.append(new)
	rst = 0
	for value in suite[::-1]:
		rst = value[0] - rst
	return rst

file = open("ref", 'r')
lines = file.read().split('\n')
rst = []
for line in lines:
	rst.append(next(line))
print(sum(rst))