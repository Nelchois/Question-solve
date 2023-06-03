#https://school.programmers.co.kr/learn/courses/30/lessons/77885
def solution(numbers):
    answer = []
    for num in numbers:
        bin_num = list(str(bin(num))[2:])
        if num % 2 == 0:
            bin_num[-1] = '1'
            answer.append(int("".join(bin_num), 2))
            continue
        else:
            Flag = False
            for idx, n in reversed(list(enumerate(bin_num))):
                if n == '0':
                    bin_num[idx] = '1'
                    bin_num[idx + 1] = '0'
                    answer.append(int("".join(bin_num), 2))
                    Flag = True
                    break
            if Flag == False:
                bn = ''.join(bin_num)
                ans = '10' + bn[1:]
                answer.append(int(ans, 2))
    return answer