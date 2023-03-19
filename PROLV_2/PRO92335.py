#https://school.programmers.co.kr/learn/courses/30/lessons/92335
def prime(n, k):
    base = ''
    while n > 0:
        n, q = divmod(n, k)
        base += str(q)
    return base[::-1]

def ck_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    prime_n = prime(n,k)
    num_list = prime_n.split('0')
    answer = 0
    for i in num_list:
        if len(i) != 0:
            i = int(i)
            if ck_prime(i) == True:
                answer += 1

    return answer