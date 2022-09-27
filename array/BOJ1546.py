from re import sub
import sys
subject_num = int(sys.stdin.readline().rstrip())
scores = list(map(int, sys.stdin.readline().split(' ')))
best_score = max(scores)
new_scores = []
for _ in range(subject_num):
    rebuild = (scores[_] / best_score) * 100
    new_scores.append(rebuild)
print(sum(new_scores)/subject_num)
