file = 'day2.txt'


# col A ---> A for Rock, B for Paper, and C for Scissors
# col B ---> X for Rock, Y for Paper, and Z for Scissors
# round ---> 1 for Rock, 2 for Paper, and 3 for Scissors
# round outcome --->  0 if you lost, 3 if the round was a draw, and 6 if you won

colA = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
colB = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
genScore = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
roundScore = {'Lost': 0, 'Draw': 3, 'Win': 6}
colBOut = {'X': 'Lost', 'Y': 'Draw', 'Z': 'Win'}


def readFile(f_in):
    with open(f_in) as f:
        data = f.readlines()
        f.close()
    return data


def rockPaperScissors(round_action):
    opp, user = round_action.strip().split()
    opp = colA[opp]
    user = colB[user]
    if opp == user:
        # tie
        return roundScore['Draw']+genScore[user]
    elif user == 'Rock':
        if opp == 'Scissors':
            # win
            return roundScore['Win']+genScore[user]
        else:
            # lose
            return genScore[user]
    elif user == 'Paper':
        if opp == 'Rock':
            # win
            return roundScore['Win']+genScore[user]
        else:
            # lose
            return genScore[user]
    elif user == 'Scissors':
        if opp == 'Paper':
            # win
            return roundScore['Win']+genScore[user]
        else:
            # lose
            return genScore[user]


def rockPaperScissorsOut(round_action):
    opp, outcome = round_action.strip().split()
    opp = colA[opp]
    outcome = colBOut[outcome]
    if outcome == 'Draw':
        return roundScore['Draw']+genScore[opp]
    elif outcome == 'Lost':
        if opp == 'Rock':
            return genScore['Scissors']
        elif opp == 'Paper':
            return genScore['Rock']
        else:
            return genScore['Paper']
    elif outcome == 'Win':
        if opp == 'Rock':
            return roundScore['Win']+genScore['Paper']
        elif opp == 'Scissors':
            return roundScore['Win']+genScore['Rock']
        elif opp == 'Paper':
            return roundScore['Win']+genScore['Scissors']


def main(action=None, game=None):
    if action == 'test':
        fileName = 'test.txt'
    else:
        action = 'regular'
        fileName = file
    totalScore = 0
    data = readFile(fileName)
    if game is None:
        for line in data:
            score = rockPaperScissors(line)
            totalScore += score
    else:
        for line in data:
            score = rockPaperScissorsOut(line)
            totalScore += score

    print(action, game, totalScore)

    return


if __name__ == '__main__':
    main('test')
    main(action=None)
    main('test', 'v2')
    main(action=None, game='v2')
