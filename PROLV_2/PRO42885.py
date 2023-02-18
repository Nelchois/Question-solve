#https://school.programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    big = 0
    small = len(people) - 1
    while big < small:
        if people[big] + people[small] <= limit:
            small -= 1
            answer += 1
        big += 1
    return len(people) - answer