import sys
n, k = map(int, sys.stdin.readline().split(' '))
score_list = list(map(int, sys.stdin.readline().split(' ')))
for i in range(k):
    cut_line = max(score_list)
    score_list.remove(cut_line)
print(cut_line)
