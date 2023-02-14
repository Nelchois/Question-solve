def solution(s):
    board = ''
    count = 0
    answer = []
    while True:
        if s == '1':
            break
        else:
            for num in s:
                if num == '1':
                    board += num
            ans = len(s) - len(board)
            answer.append(ans)
            s = bin(len(board))[2:]
            board = ''
            count += 1
    ans = [count, sum(answer)]
    return ans
