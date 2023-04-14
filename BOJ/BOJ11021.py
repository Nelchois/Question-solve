i=int(input())
n=1
for _ in range(i):
    a,b=map(int,input().split())
    print(f'Case #{n}:', a+b)
    n+=1