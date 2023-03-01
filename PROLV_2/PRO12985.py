#https://school.programmers.co.kr/learn/courses/30/lessons/12985
def cal(a, b):
    if a % 2 != 0:
        a = (a+1)//2
    else:
        a //= 2
    if b % 2 != 0:
        b = (b+1)//2
    else:
        b //= 2
    return a, b
def solution(n,a,b):
    answer = 0
    while True:
        n //= 2 
        if (a <= n and b <= n) or (a > n and b > n):
            ab = []
            while True:
                ab.append(a)
                ab.append(b)
                if abs(a-b) == 1 and min(ab) % 2 != 0:
                    answer += 1
                    return answer
                else:
                    a, b = cal(a, b)
                    answer += 1
        else:
            if abs(a - b) == 1:
                if (a+b) // 2 == n:
                    cnt = 1
                    while n != 1:
                        n //= 2
                        cnt += 1
                    answer += cnt
                while n != 1:
                    ab = []
                    ab.append(a)
                    ab.append(b)
                    if min(ab) % 2 == 0:
                        answer += 1
                        a, b = cal(a, b)
                    else:
                        answer += 1
                        break
                break
            a, b = cal(a, b)
            answer += 1
    return answer