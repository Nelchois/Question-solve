Foul = list(input().split())
Foul_dic = {}
for _ in Foul:
    if _ in Foul_dic:
        Foul_dic[_] +=1
    else:
        Foul_dic[_] = 1
print(*[k for k,v in Foul_dic.items() if min(Foul_dic.values()) == v], min(Foul_dic.values()), sep='\n')