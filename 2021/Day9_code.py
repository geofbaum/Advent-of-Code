ll = [[int(y) for y in x] for x in open('Day9_data.txt').read().strip().split('\n')]
s=0
for i in range(len(ll)):
	for j in range(len(ll[0])):
		if i>0 and ll[i][j] >= ll[i-1][j]:
			continue
		if i<len(ll)-1 and ll[i][j] >= ll[i+1][j]:
			continue
		if j>0 and ll[i][j] >= ll[i][j-1]:
			continue
		if j<len(ll[0])-1 and ll[i][j] >= ll[i][j+1]:
			continue
		s += ll[i][j]+1
print('Part 1 Answer is: ',s)

from collections import Counter
ll = [[int(y) for y in x] for x in open('Day9_data.txt').read().strip().split('\n')]

def basin(i,j):
	downhill = None
	for (di, dj) in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
		if di in range(len(ll)) and dj in range(len(ll[0])):
			if ll[i][j] > ll[di][dj]:
				downhill = (di, dj)
	if downhill is None:
		return (i, j)
	ret = basin(*downhill)
	return ret

basins = []
for i in range(len(ll)):
	for j in range(len(ll[0])):
		if ll[i][j] != 9:
			basins.append(basin(i, j))

ret = 1
for basin, common in Counter(basins).most_common(3):
	ret *= common
print('Part 2 Answer is: ',ret)
