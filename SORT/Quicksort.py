import sys
count = int(sys.stdin.readline().rstrip())
num_list = []
for _ in range(count):
    num_list.append(int(sys.stdin.readline().rstrip()))
def sort(num_list):
    if len(num_list) > 1:
        pivot = num_list[len(num_list)//2]
        left = []
        right = []
        middle = []
        for i in range(len(num_list)):
            if num_list[i] < pivot:
                left.append(num_list[i])
            elif num_list[i] > pivot:
                right.append(num_list[i])
            else:
                middle.append(num_list[i])
        return sort(left) + middle + sort(right)
    else:
        return num_list
ans_list = sort(num_list)
for n in range(count):
    print(ans_list[n])
    