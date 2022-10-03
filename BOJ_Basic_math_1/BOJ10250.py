import sys
test_case = int(sys.stdin.readline().rstrip())
for _ in range(test_case):
    H, W, N = map(int, sys.stdin.readline().rstrip().split(' '))
    room_num = N//H 
    hight = N%H
    if N <= H:
        room_num = 1
        hight = N
    elif (N > H) and (N%H > 0):
        room_num = N//H + 1
        hight = N%H
    elif (N > H) and (N%H == 0):
        room_num = N//H
        hight = H
    final_room = f'{hight*100 + room_num}'
    print(final_room)
