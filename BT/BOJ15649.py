import sys
n, m = map(int, sys.stdin.readline().rstrip().split(' '))
number_list = [i for i in range(1, n + 1)]
number_line = []
def make_line():
    if len(number_line) == m:
        print(' '.join(map(str, number_line)))
        return
    for i in range(1, n + 1):
        if i not in number_line:
            number_line.append(i)
            make_line()
            number_line.pop()

make_line()
