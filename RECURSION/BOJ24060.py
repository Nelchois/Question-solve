import sys
n, k = map(int, sys.stdin.readline().rstrip().split(' '))
num_list = list(map(int, sys.stdin.readline().rstrip().split(' ')))
counter = []
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = (len(arr) + 1) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            counter.append(low_arr[l])
            l += 1
        
        else:
            merged_arr.append(high_arr[h])
            counter.append(high_arr[h])
            h += 1
    
    while l < len(low_arr):
        merged_arr.append(low_arr[l])
        counter.append(low_arr[l])
        l += 1

    while h < len(high_arr):
        merged_arr.append(high_arr[h])
        counter.append(high_arr[h])
        h += 1

    return merged_arr

a = merge_sort(num_list)
if len(counter) >= k:
    print(counter[k-1])
else:
    print(-1)
    