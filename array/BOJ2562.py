comprehension_list = [int(input()) for i in range(9)]
print(max(comprehension_list), comprehension_list.index(
    max(comprehension_list))+1, sep='\n')
