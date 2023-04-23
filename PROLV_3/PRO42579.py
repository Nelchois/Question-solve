#https://school.programmers.co.kr/learn/courses/30/lessons/42579music = dict()
music = dict()
gen = dict()
def solution(genres, plays):
    answer = []
    m_num = len(genres)
    for i in range(m_num):
        g = genres[i]
        count = plays[i]
        if g not in music:
            music[g] = [(i, count)]
        else:
            music[g].append((i, count))
        if g in gen:
            gen[g] += count
        else:
            gen[g] = count
    sort_gen = sorted(gen.items(), key = lambda x: x[1], reverse = True)
    for li in sort_gen:
        key = li[0]
        category = music[key]
        if len(category) == 1:
            answer.append(category[0][0])
            continue
        elif len(category) > 1:
            category.sort(key = lambda x: x[1])
            alpha = category.pop()
            beta = category.pop()
            if alpha[1] == beta[1]:
                if alpha[0] < beta[0]:
                    answer.append(alpha[0])
                    answer.append(beta[0])
                else:
                    answer.append(beta[0])
                    answer.append(alpha[0])
            else:
                answer.append(alpha[0])
                answer.append(beta[0])  
    return answer