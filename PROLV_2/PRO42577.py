#https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    answer = True
    if len(phone_book) == 1:
        return answer
    phone_book.sort(key = lambda x: x)
    for i in range(len(phone_book) - 1):
        short_number = phone_book[i]
        n = len(short_number)
        long_number = phone_book[i + 1][0: n]
        if short_number == long_number:
            answer = False
            return answer
    return answer
    
    