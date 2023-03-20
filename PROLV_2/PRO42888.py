#https://school.programmers.co.kr/learn/courses/30/lessons/42888#
def solution(record):
    answer = []
    board = dict()
    ans_list = []
    for i in record:
        command_list = i.split(' ')
        com = command_list[0]
        uid = command_list[1]
        if com == "Enter" or com == "Change":
            name = command_list[2]
            board[uid] = name
            if com == "Enter":
                ans_list.append([uid, 'E'])
        else:
            ans_list.append([uid, 'L'])

            
    for j in ans_list:
        uid = j[0]
        status = j[1]
        if status == 'E':
            answer.append(f"{board[uid]}님이 들어왔습니다.")
        elif status == 'L':
            answer.append(f"{board[uid]}님이 나갔습니다.")
    
    return answer