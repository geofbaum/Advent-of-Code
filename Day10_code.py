def part1(input_):
    ll = [x for x in open(input_).read().strip().split('\n')]

    matches = {'[': ']', '{': '}', '<': '>', '(': ')'}
    costs = {']': 57, ')': 3, '}': 1197, '>': 25137}
    starters = list(matches.keys())
    for (k, v) in list(matches.items()):
        matches[v] = k
    cost = 0
    for line in ll:
        stack = []
        for ch in line:
            if ch in starters:
                stack = [ch] + stack
            else:
                if not stack:
                    break
                expected = matches[stack[0]]
                stack = stack[1:]
                if expected == ch:
                    continue
                cost += costs[ch]
                break
    print(cost)
    return

def part2(input_):
    ll = [x for x in open(input_).read().strip().split('\n')]
    print(ll)
    matches = {'[': ']', '{': '}', '<': '>', '(': ')'}
    costs = {']': 2, ')': 1, '}': 3, '>': 4}
    starters = list(matches.keys())
    for (k, v) in list(matches.items()):
        matches[v] = k
    cost = []
    for line in ll:
        stack = []
        failures = False
        for ch in line:
            if ch in starters:
                stack = [ch] + stack
            else:
                if not stack:
                    break
                expected = matches[stack[0]]
                stack = stack[1:]
                if expected == ch:
                    continue
                failures = True
                break
        if not failures:
            c = 0
            for ch in stack:
                c = c * 5 + costs[matches[ch]]
            cost += [c]

    cost = sorted(cost)

    print(cost[len(cost) // 2])
    return

def main():
    input_ = 'day10.txt'
    part1(input_)
    part2(input_)

    return

if __name__ == '__main__':
    main()
