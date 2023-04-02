def solution(n):
    answer = ''
    while True:
        if n == 0:
            break
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
    return answer