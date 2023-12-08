file = open("ref", 'r')
line = file.read().split('\n')
# time = [int(i) for i in line[0].split(':')[1].strip().split(' ') if i != ''] 
# dist =[int(i) for i in line[1].split(':')[1].strip().split(' ') if i != '']
time = line[0].split(':')[1].replace(' ', '')
dist = line[1].split(':')[1].replace(' ', '')
print (time)
print(dist)
rst = 1
# for i, j in enumerate(time):
	# t = int(time[i])
	# d = int(dist[i])
wtw = 0
for x in range(0, int(time) + 1):
	par = x * (int(time) - x)
	if (par > int(dist)):
		wtw += 1
rst *= wtw
print(rst)

# programme lent pour la partie 2