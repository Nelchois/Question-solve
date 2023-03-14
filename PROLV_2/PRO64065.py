#https://school.programmers.co.kr/learn/courses/30/lessons/64065
num_dic = dict()
board = []
def solution(s):
    for i in s:
        if i == '{':
            continue
        if (i == '}' or i == ',') and len(board) > 0:
            key = ''.join(board)
            if key in num_dic:
                num_dic[key] += 1
            else:
                num_dic[key] = 1
            board.clear()
        else:
            if i != ',':
                board.append(i)
    sort_d = sorted(num_dic.items(), key = lambda x: x[1], reverse = True)
    answer = []
    for tu in sort_d:
        answer.append(int(tu[0]))
    
    return answer
