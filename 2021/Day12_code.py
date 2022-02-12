alphabet = 'abcdefghijklmnopqrstuvwxyz'
from collections import defaultdict

inf = 'day12.txt'

ll = [x for x in open(inf).read().strip().split('\n')]

edges = defaultdict(list)
for line in ll:
	x, y = line.split("-")
	edges[x].append(y)
	edges[y].append(x)

def issmall(c):
	return c != 'end' and c[0] in alphabet

def search(curr, visitedsmall):
	if curr == 'end':
		return 1
	cnt = 0
	for nxt in edges[curr]:
		if issmall(nxt):
			if nxt not in visitedsmall:
				cnt += search(nxt, visitedsmall | set([nxt]))
		else:
			cnt += search(nxt, visitedsmall)
	return cnt
print(search('start', set(['start'])))

def search2(curr, v1, visitedsmalltwice):
	if curr == 'end':
		return 1
	cnt = 0
	for nxt in edges[curr]:
		if nxt == 'start':
			continue
		if issmall(nxt):
			if nxt in v1:
				if not visitedsmalltwice:
					cnt += search2(nxt, v1, True)
			else:
				cnt += search2(nxt, v1 | set([nxt]), visitedsmalltwice)
		else:
			cnt += search2(nxt, v1, visitedsmalltwice)
	return cnt
print(search2('start', set(), False))
