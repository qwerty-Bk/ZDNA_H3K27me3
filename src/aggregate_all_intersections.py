import os


def wc(f):
    res = 0
    with open(f) as ff:
        for l in ff:
            res += 1
    return res

res = [[] for i in range(9)]

for f in os.listdir('.'):
    if len(f) != 8 + 4:
        continue
    cnt = 0
    for i in range(8):
        if f[i] == '1':
            cnt += 1
    w = wc(f)
    if w != 0:
        res[cnt].append((w, f))

for i in range(9):
    print(i)
    res[i].sort(reverse=True)
    print(' '.join(map(str, res[i])))
