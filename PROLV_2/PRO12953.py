#https://school.programmers.co.kr/learn/courses/30/lessons/12953
def solution(arr):
    answer = 0
    arr.sort()
    big = arr.pop()
    ck_num = big * 1
    while True:
        if answer != 0:
            break
        for i in arr:
            if ck_num % i != 0:
                ck_num += big
                break
            elif arr[-1] == i:
                answer += ck_num
    return answer