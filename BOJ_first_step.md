These codes for first_step in baekjoon.
From 10869 ~ 25083 are arithmetic operation example.
```
#baekjoon10869
A, B = input().split(' ')
print(int(A) + int(B))
print(int(A) - int(B))
print(int(A) * int(B))
print(int(A) // int(B))
print(int(A) % int(B))

#baek 10926
check_id = input()
print(f'{check_id}??!')

#baek 18108
bud_cal = int(input())
print(bud_cal - 543)

#baek 3003
haved_set = list((input().split(' ')))
haved_set = list(map(int, haved_set))
perfect_set = [1, 1, 2, 2, 2, 8]
lack_of_set= [perfect_set[i] - haved_set[i] for i in range(len(haved_set))]
print(*lack_of_set)

#baek10430
A, B, C = map(int, input().split(' '))
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

#baek2588
A = int(input())
B = int(input())
print(A * (B % 10), A * (B // 10 % 10), A * (B // 100), A * B, sep= '\n')

#baek10171
print('\\    /\\')
print(" )  ( ')")
print('(  /  )')
print(' \(__)|')

#baek 10172
print("|\_/|")
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')

#baek25083
print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \\. \". L_r'")
print('   `~\\/')
print('      |')
print('      |')

#baek1330
A, B = map(int, input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')

#baek9498
Score = int(input())
if 90 <= Score <= 100:
    print('A')
elif 80 <= Score <= 89:
    print('B')
elif 70 <= Score <= 79:
    print('C')
elif 60 <= Score <= 69:
    print('D')
else:
    print('F')

#baek2753
Year = int(input())
if (Year % 4 == 0) and (Year % 100 != 0):
    print(1)
elif Year % 400 == 0:
    print(1)
else:
    print(0)

#baek 14681
X = int(input())
Y = int(input())
if (X > 0) and (Y > 0):
    print(1)
elif (X < 0) and (Y > 0):
    print(2)
elif (X < 0) and (Y < 0):
    print(3)
else:
    print(4)
```