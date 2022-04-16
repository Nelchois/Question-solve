t=int(input())
for _ in range(1,t+1):
    if _%2 != 0:
        print('* '*t)
    elif _%2 == 0:
        print(' ','* '*t,sep='')


