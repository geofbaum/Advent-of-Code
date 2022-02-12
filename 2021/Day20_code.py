with open("day20.txt") as f:
    data = f.read()

import numpy as np
from scipy.ndimage import convolve

lines = data.splitlines()
alg = [i for i, c in enumerate(lines[0]) if c == "#"]
img = np.pad(np.array([[int(c == "#") for c in l] for l in lines[2:]]), ((50, 50), (50, 50)))
rot = np.array([[1, 2, 4], [8, 16, 32], [64, 128, 256]])

for i in range(50):
    img = np.isin(convolve(img, rot, mode="constant", cval=i % 2), alg).astype(int)
    if i == 1:
        print("part1", img.sum())

print("part2", img.sum())
