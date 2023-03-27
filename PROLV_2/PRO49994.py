#https://school.programmers.co.kr/learn/courses/30/lessons/49994
def solution(dirs):
    now = [0, 0]
    history = set()
    for command in dirs:
        if command == 'U' and now[1] < 5:
            new = [now[0], now[1] + 1]
            log = now + new
            log2 = new + now
            history.add(tuple(log))
            history.add(tuple(log2))
            now[1] += 1
        elif command == 'D' and now[1] > -5:
            new = [now[0], now[1] - 1]
            log = now + new
            log2 = new + now
            history.add(tuple(log))
            history.add(tuple(log2))
            now[1] -= 1
        elif command == 'R' and now[0] < 5:
            new = [now[0] + 1, now[1]]
            log = now + new
            log2 = new + now
            history.add(tuple(log))
            history.add(tuple(log2))
            now[0] += 1
        elif command == 'L' and now[0] > -5:
            new = [now[0] - 1, now[1]]
            log = now + new
            log2 = new + now
            history.add(tuple(log))
            history.add(tuple(log2))
            now[0] -= 1
    answer = len(history)//2
    return answer