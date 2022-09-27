import sys
case_num = int(sys.stdin.readline().rstrip())
for i in range(case_num):
    case = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    people = case.pop(0)
    if people != 0:
        mean_score = sum(case)/people
        over_mean_list = [score for score in case if score > mean_score]
        over_mean_rate = (len(over_mean_list)/len(case)) * 100 
        print(f'{over_mean_rate:.3f}%', sep='')
    elif (sum(case) == 0) or (people == 0):
        print('0.000%')