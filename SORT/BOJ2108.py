
import sys
from collections import Counter
count = int(sys.stdin.readline())
num_list = []
for i in range(count):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()
cnt = Counter(num_list).most_common(2)
ans_2 = f'{sum(num_list)/count:.0f}'
if ans_2 == '-0':
    ans_2 = 0
print(ans_2)
print(num_list[count//2])
if len(num_list) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(num_list) - min(num_list))