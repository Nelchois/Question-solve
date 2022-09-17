These codes are answer from Baekjoon_1330 to Baekjoon_2480 that using ```if```.
```
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

#baek2884
hour, minute = map(int, input().split(' '))
if (hour == 0) and (minute < 45):
    hour = 24
if 45 - minute < 0:
    print(f'{hour} {minute - 45}')
elif 45 - minute > 0:
    print(f'{hour - 1} {60 - (45 - minute)}')
elif minute == 45:
    print(f'{hour} {0}')

#baek2525
hour, minute = map(int, input().split(' '))
cooking_time = int(input())
spend_hour = (cooking_time + minute) // 60 
spend_minute = (cooking_time + minute) % 60 
if hour + spend_hour > 24:
    print(f'{hour + spend_hour - 24} {spend_minute}')
elif hour + spend_hour == 24:
    print(f'{0} {spend_minute}')
elif hour + spend_hour < 24:
    print(f'{hour + spend_hour} {spend_minute}')

#baek2480
num1, num2, num3 = map(int, input().split(' '))
num_list = [num1, num2, num3]
if (num1 == num2) and (num2 == num3):
    print(10000 + num1 * 1000)
elif (num1 == num2) or (num2 == num3) or (num1 == num3):
    if num1 == num2:
        print(1000 + num1 * 100)
    elif num2 == num3:
        print(1000 + num2 * 100)
    elif num1 == num3:
        print(1000 + num1 * 100)
elif (num1 != num2) and (num2 != num3) and (num1 != num3):
    print(max(num_list) * 100)
```