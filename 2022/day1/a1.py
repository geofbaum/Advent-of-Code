file = '2022_day1_data.txt'


def readFile(f_in):
    with open(f_in) as f:
        data = f.readlines()
        f.close()
    return data


def prepData(data):
    elf = 0
    calData = {}
    cal = 0
    for line in data:
        line = line.strip()
        if line:
            cal += int(line)
        else:
            calData[elf] = cal
            elf += 1
            cal = 0

    return calData


def answer1(calData):
    return max(calData, key=calData.get)


def answer2(calData, n):
    sortTop = dict(sorted(calData.items(), key=lambda item: item[1], reverse=True)[:n])
    topN = 0
    for v in sortTop.values():
        topN += v

    return topN


def main():
    data = readFile(file)
    data_p = prepData(data)

    a1 = answer1(data_p)
    print('The elf with the most calories is elf {0} with {1} calories.'.format(a1, data_p[a1]))

    topN = 3
    a2 = answer2(data_p, topN)
    print('The top {0} elves have a combined calorie total of {1} calories.'.format(topN, a2))

    return


if __name__ == '__main__':
    main()
