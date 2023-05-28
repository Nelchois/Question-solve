#https://school.programmers.co.kr/learn/courses/30/lessons/12936
#https://readydeveloperone.blogspot.com/2023/05/12936.html
def total(n):
    if n > 1:
        return n*total(n-1)
    elif n == 1:
        return 1
    
def order(o, k, n):
    t = total(n - o)
    num = 1
    while k > t:
        k -= t
        num += 1
    return num, k

def solution(n, k):
    answer = []
    num_list = [i for i in range(1, n + 1)]
    o = 1
    while o < n: 
        st, k = order(o, k, n)
        st = num_list.pop(st - 1)
        answer.append(st)
        o += 1
    answer.append(num_list[0])
    return answer