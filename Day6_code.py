import fileinput
from collections import defaultdict

def p1(in_):
    return f(in_, 80)

def p2(in_):
    return f(in_, 256)

def f(x, n):
    state = defaultdict(int)
    for fish in x:
        state[fish] += 1
    for _ in range(n):
        state = g(state)

    return sum(state.values())

def g(x):
    ns = defaultdict(int)
    for i, n in x.items():
        if i == 0:
            ns[6] += n
            ns[8] += n
        else:
            ns[i-1] += n
    return ns

def main():
    in_ = list(map(int, next(fileinput.input('C:\\Users\\Ge007543\\Documents\\day6.txt')).split(',')))
    print(p1(in_))
    print(p2(in_))

if __name__ == '__main__':
    main()
