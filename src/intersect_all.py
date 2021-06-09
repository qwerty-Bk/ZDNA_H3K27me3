import os


def int2(a, b, o):
    os.system(f'bedtools intersect -a {a} -b {b} > {o}')


def name(mask):
    s = str(bin(mask))[2:]
    return '0' * (8 - len(s)) + s


files = [
    'C2C12_antonov.bed',
    'H1_anoprenko.bed',
    'MCF-7_bulatova.bed',
    'SK-N-SH_plechova.bed',
    'GM12878_romanchenko.bed',
    'H7_grachev.bed',
    'MEL_sibagatova.bed',
    'h1_gudiev.bed'
]

n = len(files)
print(n)

for i in range(n):
    nm = name(2 ** i)
    os.system(f'cp {files[i]} {nm}.bed')

for i in range(1, 2 ** n):
    s = name(i)
    cnt = 0
    for x in s:
        if x == '1':
            cnt += 1

    if cnt < 2:
        continue

    nn = ''
    s1 = list(s)
    for x in range(len(s)):
        if s[7 - x] == '1':
            s1[7 - x] = '0'
            nn = name(2 ** x)
            break
    s1 = ''.join(s1)

    int2(f'{s1}.bed', f'{nn}.bed', f'{s}.bed')

