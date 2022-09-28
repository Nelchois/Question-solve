import sys
word = sys.stdin.readline().rstrip()
dial_time = 0
for _ in range(len(word)):
    if word[_] in 'ABC':
        dial_time += 3
    elif word[_] in 'DEF':
        dial_time += 4
    elif word[_] in 'GHI':
        dial_time += 5
    elif word[_] in 'JKL':
        dial_time += 6
    elif word[_] in 'MNO':
        dial_time += 7
    elif word[_] in 'PQRS':
        dial_time += 8
    elif word[_] in 'TUV':
        dial_time += 9
    elif word[_] in 'WXYZ':
        dial_time += 10
print(dial_time)