#https://school.programmers.co.kr/learn/courses/30/lessons/12941
ans = [0]
def solution(A, B):
    a = sorted(A)
    b = sorted(B)
    for i in range(len(A)):
        ans[0] += a.pop(0) * b.pop()
    return ans[0]
                


