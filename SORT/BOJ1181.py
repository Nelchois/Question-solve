import sys
from string import ascii_lowercase
num = int(sys.stdin.readline())
ck_list = []
score = dict()
for i in range(num):
    word = sys.stdin.readline().rstrip()
    ck_list.append([word, len(word)])
alpha = list(ascii_lowercase)
for _ in range(len(alpha)):
    score[alpha[_]] = _
def sort(ck_list):
    left = []
    right = []
    middle = []
    if len(ck_list) > 1:
        pivot = ck_list[len(ck_list)//2]
        for n in range(len(ck_list)):
            ck_num = ck_list[n]
            if ck_num[0] == pivot[0]:
                continue
            else:
                if pivot[1] > ck_num[1]:
                    left.append(ck_num)
                elif pivot[1] < ck_num[1]: 
                    right.append(ck_num)
                else:
                    for m in range(pivot[1]):
                        ck_al = ck_num[0][m]
                        pi_al = pivot[0][m]
                        if ck_al == pi_al:
                            continue
                        elif ck_al != pi_al:
                            if score[ck_al] > score[pi_al]:
                                right.append(ck_num)
                                break
                            elif score[ck_al] < score[pi_al]:
                                left.append(ck_num)
                                break
                        else:
                            continue
        middle.append(pivot)
        return sort(left) + middle + sort(right)
    else:
        return ck_list

ans = sort(ck_list)
for j in range(len(ans)):
    print(ans[j][0])
