from ast import comprehension


standard_num = int(input())
'''list_num = []
for _ in range(1, standard_num+1):
    list_num.append(_*_)
print(list_num)
'''
comprehension_numbers = [i*i for i in range(1, standard_num+1)]
print(comprehension_numbers)
