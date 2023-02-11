#Question Link https://school.programmers.co.kr/learn/courses/30/lessons/138476
def solution(k, tangerine):
    mandarin = dict()
    size = 0
    for i in tangerine:
        if i in mandarin:
            mandarin[i] += 1
        else:
            mandarin[i] = 1
    sor_dict = sorted(mandarin.items(), key = lambda x:x[1], reverse = True)
    while True:
        man_num = sor_dict[size][1]
        if k == 0:
            break
        if k >= man_num:
            k -= man_num
            size += 1
        elif k < man_num:
            k -= k
            size += 1
            break
        if size == len(sor_dict):
            break
    answer = size
    return answer