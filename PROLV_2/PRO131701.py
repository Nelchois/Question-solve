#https://school.programmers.co.kr/learn/courses/30/lessons/131701
number = set()
def make_num(elements, start, n):
    for cnt in range(1, n + 1):
        num_list = elements[start: start + cnt]
        number.add(sum(num_list))
    return 

def solution(elements):
    n = len(elements)
    elements *= 2
    for start in range(1, n + 1):
        make_num(elements, start, n)
    answer = len(number)
    return answer