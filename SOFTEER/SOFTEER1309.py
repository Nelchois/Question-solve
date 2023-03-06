#https://softeer.ai/practice/info.do?idx=1&eid=1309
import sys
n = int(sys.stdin.readline())
score1_list = list(map(int, sys.stdin.readline().split(' ')))
score2_list = list(map(int, sys.stdin.readline().split(' ')))
score3_list = list(map(int, sys.stdin.readline().split(' ')))
score4_list = []
person_score_dic = dict()
for i in range(n):
    a = score1_list[i]
    b = score2_list[i]
    c = score3_list[i]
    total = a + b + c
    person_score_dic[f'{i}'] = [a, b, c, total]
    score4_list.append(total)
score1_list.sort()
score2_list.sort()
score3_list.sort()
score4_list.sort()

rank1 = dict()
rank2 = dict()
rank3 = dict()
rank4 = dict()

r1 = 1
r2 = 1
r3 = 1
r4 = 1

s1 = 1001
s2 = 1001
s3 = 1001
s4 = 3001

for j in range(n):
    score1 = score1_list.pop()
    score2 = score2_list.pop()
    score3 = score3_list.pop()
    score4 = score4_list.pop()
    if s1 > score1:
        if f'{score1}' not in rank1:
            rank1[f'{score1}'] = r1
            s1 = score1
            r1 += 1
    elif s1 == score1:
        r1 += 1        

    if s2 > score2:
        if f'{score2}' not in rank2:
            rank2[f'{score2}'] = r2
            s2 = score2
            r2 += 1
    elif s2 == score2:
        r2 += 1

    if s3 > score3:
        if f'{score3}' not in rank3:
            rank3[f'{score3}'] = r3
            s3 = score3
            r3 += 1
    elif s3 == score3:
        r3 += 1

    if s4 > score4:
        if f'{score4}' not in rank4:
            rank4[f'{score4}'] = r4
            s4 = score4
            r4 += 1
    elif s4 == score4:
        r4 += 1

answer1 = []
answer2 = []
answer3 = []
answer4 = []

for person in range(n):
    s_list = person_score_dic[f'{person}']
    answer1.append(rank1[f'{s_list[0]}'])
    answer2.append(rank2[f'{s_list[1]}'])
    answer3.append(rank3[f'{s_list[2]}'])
    answer4.append(rank4[f'{s_list[3]}'])
print(*answer1)
print(*answer2)
print(*answer3)
print(*answer4)

