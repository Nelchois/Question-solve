import sys
case = int(sys.stdin.readline())
point_list = []
for i in range(case):
    point = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    point_list.append(point)
def psort(point_list):
    left = []
    right = []
    middle = []
    if len(point_list) > 1:
        pivot = point_list[int(len(point_list)//2)]
        middle.append(pivot)
        for i in range(len(point_list)):
            ck_point = point_list[i]
            if ck_point[0] < pivot[0]:
                left.append(ck_point)
            elif ck_point[0] > pivot[0]:
                right.append(ck_point)
            else:
                if pivot[1] < ck_point[1]:
                    right.append(ck_point)
                elif pivot[1] > ck_point[1]:
                    left.append(ck_point)
        return psort(left) + middle + psort(right)
    else:
        return point_list

ans = psort(point_list)
for j in range(len(ans)):
    print(*ans[j])