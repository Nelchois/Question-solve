import sys
case = int(sys.stdin.readline())
member = []
for i in range(case):
    age, name = sys.stdin.readline().rstrip().split(' ')
    member.append([int(age), name, i])
def sort(member):
    left = []
    right = []
    middle = []
    if len(member) > 1:
        pivot = member.pop(len(member)//2)
        for n in range(len(member)):
            ck = member[n]
            if ck[0] > pivot[0]:
                right.append(ck)
            elif ck[0] < pivot[0]:
                left.append(ck)
            else:
                if ck[2] < pivot[2]:
                    left.append(ck)
                elif ck[2] > pivot[2]:
                    right.append(ck)
        middle.append(pivot)
        return sort(left) + middle + sort(right)
    else:
        return member
ans = sort(member)
for _ in range(len(ans)):
    print(ans[_][0], ans[_][1])