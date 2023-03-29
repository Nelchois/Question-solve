#https://school.programmers.co.kr/learn/courses/30/lessons/17686
num_dict = {f'{i}': 0 for i in range(10)}
def solution(files):
    answer = []
    file_dict = {}
    for i, file in enumerate(files):
        head = ""
        number = ""
        for word in file:
            if len(number) > 0 and word not in num_dict:
                break
            if word in num_dict:
                number += word
            else:
                head += word
        file_dict[file] = [file, head.lower(), int(number), i]

    value = list(file_dict.values())
    sort_list = sorted(value, key = lambda x: (x[1], x[2], x[3]))
    for i in sort_list:
        answer.append(i[0])
    return answer