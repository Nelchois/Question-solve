#https://school.programmers.co.kr/learn/courses/30/lessons/12946
def hanoi(n, send, arr, sub, answer):
    if n == 1:
        answer.append([send, arr])
        return
    hanoi(n - 1, send, sub, arr, answer)
    answer.append([send, arr])
    hanoi(n - 1, sub, arr, send, answer)
                
def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer


