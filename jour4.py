file = open("ref", 'r')
lines = file.read().split('\n')
final = 0

tab_cards = []
for line in lines:
	tab_cards.append(1)

for card, line in enumerate(lines):
	curr = line.split(':')[1].strip()
	tab = curr.split('|')
	nbrs = tab[1].split(' ')
	win = tab[0].split(' ')
	rst = 0
	for nbr in nbrs:
		if nbr == '':
			continue
		if nbr in win and rst == 0:
			rst = 1
		elif nbr in win and rst > 0:
			rst += 1
	for x in range(rst):
		tab_cards[card + x + 1] += tab_cards[card]
print(sum(tab_cards))