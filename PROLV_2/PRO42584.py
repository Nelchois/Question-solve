#https://school.programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    answer = []
    for idx, price in enumerate(prices):
        time = 0
        for i in range(idx + 1, len(prices)):
            compare = prices[i]
            if price <= compare:
                time += 1
            else:
                time += 1
                break
        answer.append(time)
    return answer