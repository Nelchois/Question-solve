import sys
n = int(sys.stdin.readline())

tower_1 = [i for i in range(n)]
tower_2 = []
tower_3 = []
size = [n, 0, 0]
def tower():
    move = tower_1.pop(0)
    size[0] -= 1
    if size[2] == size[1]:
        tower_3.append(move)
        size[2] += 1
    