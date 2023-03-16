#https://school.programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    answer = []
    pro_dic = {f'{idx}': i for idx, i in enumerate(progresses)}
    for i in range(len(progresses)):
        x, y = 100 - pro_dic[f'{i}'], speeds[i]
        if x % y == 0:
            pro_dic[f'{i}'] = x // y
        else:
            pro_dic[f'{i}'] = x // y + 1
    left = list(pro_dic.values())
    cnt = 1
    ck_num = left[0]
    for i in range(1, len(left)):
        num = left[i]
        if num <= ck_num:
            cnt += 1
        else:
            ck_num = num
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
        
    return answer