import itertools

def part1(s):
	c = 0
	for line in s:
    		a,b = line.split(" | ")
    		b = b.split(" ")
	    	for x in b:
        		if len(x) in (2,3,4,7):
            		c += 1
	print(c)
	return

def part2(s):
	m = {"acedgfb":8, "cdfbe":5, "gcdfa":2, "fbcad":3, "dab":7,
         "cefabd":9, "cdfgeb":6, "eafb":4, "cagedb":0, "ab":1}

	m = {"".join(sorted(k)):v for k,v in m.items()}

	ans = 0
	for line in s:
    		a,b = line.split(" | ")
    		a = a.split(" ")
   		b = b.split(" ")
    		for perm in itertools.permutations("abcdefg"):
        		pmap = {a:b for a,b in zip(perm,"abcdefg")}
        		anew = ["".join(pmap[c] for c in x) for x in a]
        		bnew = ["".join(pmap[c] for c in x) for x in b]
        		if all("".join(sorted(an)) in m for an in anew):
            			bnew = ["".join(sorted(x)) for x in bnew]
            			ans += int("".join(str(m[x]) for x in bnew))
            			break
	print(ans)
	return

def main():
	with open("C:\\Users\\Ge007543\\Documents\\day8.txt") as f:
    		s = f.read().strip().split("\n")
	print(part1(s))
	print(part2(s))

if __name__ == '__main__':
	main()
