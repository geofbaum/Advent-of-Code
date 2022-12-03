from more_itertools import chunked
fileR = 'day3.txt'
fileT = 'test.txt'


def splitString(line):
    p1, p2 = line[:len(line)//2], line[len(line)//2:]
    return p1, p2


def readFile(f_in):
    with open(f_in) as f:
        data = f.read().split('\n')
        f.close()
    return data


def scoring(s, score):
    for ss in s:
        if str.islower(ss):
            score += ord(ss) - ord('a') + 1
        else:
            score += ord(ss) - ord('A') + 27
    return score


def a1(data, score):
    for line in data:
        f, s = splitString(line)
        s1 = set(f) & set(s)
        score = scoring(s1, score)
    return score


def a2(data, score):
    for line in chunked(data, 3):
        s = set(line[0]) & set(line[1]) & set(line[2])
        score = scoring(s, score)
    return score


def main(f_in):
    data = readFile(f_in)
    score = 0
    print('Answer 1: ', a1(data, score))
    score2 = 0
    print('Answer 2: ', a2(data, score2))

    return


if __name__ == '__main__':
    print('Test File')
    main(fileT)
    print('Main File')
    main(fileR)
