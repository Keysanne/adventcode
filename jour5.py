file = open("ref", 'r')
lines = file.read().split('\n')
number = lines.pop(0).split(':')[1].strip().split(' ')
numbers = [] 
for x in range(0, len(number) - 1, 2):
	numbers.extend([n for n in range(int(number[x]), int(number[x]) + int(number[x + 1]))])
nbr_ch = []
for x in numbers:
	nbr_ch.append(0)
for line in lines:
	line = line.split(' ')
	if line[0].isdigit():
		for index, x in enumerate(numbers):
			if int(x) >= int(line[1]) and int(x) < int(line[1]) + int(line[2]) and nbr_ch[index] == 0:
				numbers[index] = int(x) + (int(line[0]) - int(line[1]))
				nbr_ch[index] = 1
	else:
		for x in numbers:
			nbr_ch[numbers.index(x)] = 0
print(min(numbers))