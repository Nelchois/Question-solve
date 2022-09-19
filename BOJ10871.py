import sys
line, standard = map(int, sys.stdin.readline().split(' '))
check_list = list(map(int, sys.stdin.readline().split(' ')))
num_list = []
for _ in range(line):
    if check_list[_] < standard:
        num_list.append(check_list[_])
    else:
        continue
print(*num_list)