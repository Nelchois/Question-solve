#https://school.programmers.co.kr/learn/courses/30/lessons/12904#qna
def even(num_dict, base, le_base, n):
    if le_base > n - base - 1:
        lim = n - base - 1
    else:
        lim = le_base
    left, right = num_dict[str(base - 1)], num_dict[str(base)]
    length = 0
    if left == right:
        length += 2
        for i in range(lim):
            le_base -= 1
            base += 1
            if num_dict[str(le_base)] == num_dict[str(base)]:
                length += 2
            else:
                break
    return length

def odd(num_dict, base, n):
    le_base, ri_base = base - 1, base + 1
    if n - 1 - ri_base >= le_base:
        lim = le_base
    else:
        lim = n - 1 - ri_base
    left, right = num_dict[str(le_base)], num_dict[str(ri_base)]
    length = 0
    if left == right:
        length += 3
        for i in range(lim):
            le_base -= 1
            ri_base += 1
            if num_dict[str(le_base)] == num_dict[str(ri_base)]:
                length += 2
            else:
                break
    return length

def solution(s):
    num_dict = dict()
    n = len(s)
    answer = 0
    for idx, alpha in enumerate(s):
        num_dict[str(idx)] = alpha
    for base in range(1, len(s) - 1):
        a = even(num_dict, base, base - 1, n)
        b = odd(num_dict, base, n)
        ans = max(a, b)
        if ans > answer:
            answer = ans
    if answer == 0:
        answer += 1
    return answer