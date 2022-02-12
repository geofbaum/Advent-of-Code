inp ='Day13.txt'

#part1
dotsl, folds = [x for x in open(inp).read().strip().split('\n\n')]

dots = set()
for line in dotsl.split("\n"):
	x,y = line.split(",")
	dots.add((int(x), int(y)))

def foldx(p, x):
	res = set()
	for pos in p:
		if pos[0]<x:
			res.add(pos)
		else:
			res.add((2*x-pos[0], pos[1]))
	return res

def foldy(p, y):
	res = set()
	for pos in p:
		if pos[1]<y:
			res.add(pos)
		else:
			res.add((pos[0], 2*y-pos[1]))
	return res

for inst in folds.split("\n")[:1]:
	d,amt = inst.split()[2].split("=")
	if d == 'x':
		dots = foldx(dots, int(amt))
	else:
		dots = foldy(dots, int(amt))
	print(len(dots))

#part2
dotsl, folds = [x for x in open(inp).read().strip().split('\n\n')]

dots = set()
for line in dotsl.split("\n"):
	x,y = line.split(",")
	dots.add((int(x), int(y)))

def foldx(p, x):
	res = set()
	for pos in p:
		if pos[0]<x:
			res.add(pos)
		else:
			res.add((2*x-pos[0], pos[1]))
	return res

def foldy(p, y):
	res = set()
	for pos in p:
		if pos[1]<y:
			res.add(pos)
		else:
			res.add((pos[0], 2*y-pos[1]))
	return res

for inst in folds.split("\n"):
	d,amt = inst.split()[2].split("=")
	if d == 'x':
		dots = foldx(dots, int(amt))
	else:
		dots = foldy(dots, int(amt))

ys = [pos[1] for pos in dots]
xs = [pos[0] for pos in dots]
for y in range(min(ys), max(ys)+1):
	s = ""
	for x in range(min(xs), max(xs)+1):
		if (x,y) in dots:
			s += "X"
		else:
			s += " "
	print(s)
print()
