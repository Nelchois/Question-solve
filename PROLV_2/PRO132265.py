#https://school.programmers.co.kr/learn/courses/30/lessons/132265
def solution(topping):
    answer = 0
    total = dict()
    for top in range(len(topping)):
        key = str(topping[top])
        if key in total:
            total[key] += 1
        else:
            total[key] = 1
    left = set()
    for i in topping:
        k = str(i)
        left.add(i)
        if total[k] != 0:
            total[k] -= 1
            if total[k] == 0:
                del total[k]
        if len(total) == len(left):
            answer += 1
    return answer