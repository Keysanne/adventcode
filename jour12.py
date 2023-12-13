def	combinaison(line, keys):
	key = []
	key = [int(x)for x in keys.split(',')]
	print(line, key, sum(key))

	return 0

file = open("ref", 'r')
lines = file.read().split('\n')
rst = 0
for line in lines:
	rst += combinaison(line.split(' ')[0], line.split(' ')[1])
# print(rst)