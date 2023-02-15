def solution(skill, skill_trees):
    answer = 0
    num = 0
    checker = True
    for tree in skill_trees:
        for i in range(len(tree)):
            forward = skill[num]
            each_sk = tree[i]
            if each_sk in skill: 
                if each_sk == forward:
                    if num < len(skill) - 1:
                        num += 1
                else:
                    checker = False
                    break
        if checker == True:
            answer += 1
        else:
            checker = True
        num = 0   
    return answer