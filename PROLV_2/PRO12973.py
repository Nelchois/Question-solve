#https://school.programmers.co.kr/learn/courses/30/lessons/12973
ri = []
def solution(s):
    answer = -1
    ans = check(s)
    if ans == True:
        answer += 2
    else:
        answer += 1      
    return answer

def check(s):
    for i in s:
        if len(ri) != 0:
            if ri[-1] == i:
                ri.pop()
            else:
                ri.append(i)           
        elif len(ri) == 0:
            ri.append(i)        
    if len(ri) == 0:
        ans = True
    else:
        ans = False
    return ans