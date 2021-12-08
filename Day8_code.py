from itertools import permutations

def part1(lines):
    count = 0
    d = {2: 1, 4: 4, 3: 7, 7: 8}
    for line in lines:
        line = line.strip()
        line = line.split(" | ")[1]
        count += sum(1 for word in line.split() if len(word) in d)
    return count

def part2(lines):
    known = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
    known2 = {o: i for (i, o) in enumerate(known)}

    count = 0
    for line in lines:
        line = line.strip()
        inp = line.split(" | ")[0]
        out = line.split(" | ")[1]

        for permute in permutations(list("abcdefg")):
            d = dict()
            for k, v in zip("abcdefg", permute):
                d[k] = v

            found = True

            for word in inp.split():
                new = "".join(sorted([d[el] for el in word]))
                if new not in known:
                    found = False
                    break

            if found:
                digits = ""
                for word in out.split():
                    real_out = "".join(sorted([d[el] for el in word]))
                    digits += str(known2[real_out])

                count += int(digits)
                break


    return count

def main():
	with open("day8.txt") as f:
		s = f.readlines()
	print(part1(s))
	print(part2(s))

if __name__ == '__main__':
	main()
