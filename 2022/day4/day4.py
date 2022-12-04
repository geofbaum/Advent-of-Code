import re

fileR = 'data.txt'
fileT = 'test.txt'


def readFile(f_in):
    with open(f_in) as f:
        data = f.read().split('\n')
        f.close()
    return data


def a1(ab, cd):
    # print to test logic is expected for test
    # print(ab <= cd or cd <= ab)
    return ab <= cd or cd <= ab


def a2(ab, cd):
    # print to test logic is expected for test
    # print(any(ab & cd))
    return any(ab & cd)


def main(f_in):
    answer1 = 0
    answer2 = 0
    data = readFile(f_in)
    for _l in data:
        a, b, c, d = map(int, re.findall(r'\d+', _l))
        ab = set(range(a, b+1))
        cd = set(range(c, d+1))
        # print(ab, cd)
        answer1 += a1(ab, cd)
        answer2 += a2(ab, cd)
    print('Answer 1: ', answer1)
    print('Answer 2: ', answer2)

    return


if __name__ == '__main__':
    print("response from test data")
    main(fileT)
    print('response from full data')
    main(fileR)
