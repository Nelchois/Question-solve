#https://school.programmers.co.kr/learn/courses/30/lessons/131127
def solution(want, number, discount):
    answer = 0
    want_dict = {f"{name}": i for i, name in enumerate(want)}
    idx = 0
    number = tuple(number)
    while idx + 10 <= len(discount):
        ck_list = list(number) 
        for i in range(idx, idx + 10):
            pro = discount[i]
            if pro in want_dict:
                if ck_list[want_dict[pro]] > 0:
                    ck_list[want_dict[pro]] -= 1
                else:
                    break
            else:
                break
        if sum(ck_list) == 0:
            answer += 1 
        idx += 1
    return answer