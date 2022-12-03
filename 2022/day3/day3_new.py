score = 0

for l in open('day3.txt').read().split('\n'):
    l1, l2 = l[:len(l)//2], l[len(l)//2:]
    s = set(l1) & set(l2)
    for ss in s:
        if str.islower(ss):
            score += ord(ss) - ord('a') + 1
        else:
            score += ord(ss) - ord('A') + 27
print(score)

score = 0

from more_itertools import chunked

for l in chunked(open('day3.txt').read().split('\n'), 3):
    s = set(l[0]) & set(l[1]) & set(l[2])
    for ss in s:
        if str.islower(ss):
            score += ord(ss) - ord('a') + 1
        else:
            score += ord(ss) - ord('A') + 27

print(score)