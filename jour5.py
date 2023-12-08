file = open("ref", 'r')
lines = file.read().split('\n')
number = lines.pop(0).split(':')[1].strip().split(' ')
min = 100000000000
for x in range(0, len(number) - 1, 2):
	for numbers in range(int(number[x]), int(number[x]) + int(number[x + 1])):
		nbr_ch = 0
		for line in lines:
			line = line.split(' ')
			if line[0].isdigit():
				if numbers >= int(line[1]) and numbers < int(line[1]) + int(line[2]) and nbr_ch == 0:
					numbers += (int(line[0]) - int(line[1]))
					nbr_ch = 1
			else:
				nbr_ch = 0
		if numbers < min:
			min = numbers
print(min)