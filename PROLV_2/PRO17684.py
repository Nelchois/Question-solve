#https://school.programmers.co.kr/learn/courses/30/lessons/17684
from string import ascii_uppercase
from collections import deque
alpha = list(ascii_uppercase)
def solution(msg):
    answer = []
    dictionary = dict()
    msg = deque(list(msg))
    for idx, i in enumerate(alpha):
        dictionary[i] = idx + 1
    n = len(msg)
    for _ in range(n):
        if len(msg) > 0:
            al = msg.popleft()
        if len(msg) == 0:
            answer.append(dictionary[al])
            break
        num = dictionary[al]
        for i in range(len(msg)):
            al += msg[0]
            if al in dictionary:
                num = dictionary[al]
                if len(msg) > 0:
                    msg.popleft()
                else:
                    break
            else:
                answer.append(num)
                dictionary[al] = len(dictionary) + 1
                break
    return answer
