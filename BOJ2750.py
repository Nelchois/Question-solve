input_count = int(input())
check_list = []
for i in range(1,input_count+1):
    check_num = input()
    check_list.append(check_num)
sort_list=sorted(map(int,check_list))
for j in sort_list:
    print(j)
'''
or print(*sorted(sort_list), sep='\n')
'''
