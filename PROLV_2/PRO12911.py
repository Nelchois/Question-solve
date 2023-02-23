#https://school.programmers.co.kr/learn/courses/30/lessons/12911
def solution(n):
    answer = 0
    num = bin(n).count('1')
    big_num = n + 1
    while True:
        ck_num = bin(big_num).count('1')
        if ck_num == num:
            answer = big_num
            break
        else:
            big_num += 1
    return answer