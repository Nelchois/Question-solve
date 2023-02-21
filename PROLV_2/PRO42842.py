#https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    answer = []
    brown_len = brown//2
    for col in range(brown_len//2):
        row = brown_len - col - 2
        if col * row == yellow:
            answer.append(row + 2)
            answer.append(col + 2)
            break
        
    return answer