#https://school.programmers.co.kr/learn/courses/30/lessons/43105
def dp(triangle):
    for i in range(0, len(triangle) - 1):
        li = triangle[i]
        if len(li) > 1:
            for x in range(0, len(li) - 1):
                a, b = li[x], li[x+1]
                if a >= b:
                    triangle[i+1][x+1] += a
                else:
                    triangle[i+1][x+1] += b
            n, m = li[0], li[-1]
            triangle[i+1][0] += n
            triangle[i+1][-1] += m
        else:
            a = li[0]
            for j in range(2):
                triangle[i+1][j] += a
def solution(triangle):
    dp(triangle)
    answer = max(triangle.pop())
    return answer