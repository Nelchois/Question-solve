import sys
word = sys.stdin.readline().rstrip()
count = int(sys.stdin.readline())
total_commend = []
le = list(word)
ri = []
for i in range(count):
    total_commend.append(sys.stdin.readline().rstrip())
for i in total_commend:
    if len(le) == 0 and (i == 'L' or i == 'B'):
        continue
    elif len(ri) == 0 and i == 'D':
        continue
    elif i == 'L':
        ri.append(le.pop())
    elif 'P' in i:
        le.append(i[2])
    elif i == 'D':
        le.append(ri.pop())
    elif i == 'B':
        le.pop()
for m in range(len(ri)):
    le.append(ri.pop())
ans = ''.join(le)
sys.stdout.write(ans)
    
