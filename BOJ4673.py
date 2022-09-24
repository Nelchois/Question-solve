list_num = list(range(1, 10000))
def self_num(list_num):
    for i in range(1, 10000):
        if i < 10:
            list_num.remove(i + i)
        elif 10 <= i < 100:
            list_num.remove(i + (i//10) + (i%10))
        elif 100 <= i < 1000:
            try:
                list_num.remove(i + (i//100) + ((i%100)//10) + (i%10))
            except ValueError:
                continue
        elif 1000 <= i < 10000:
            try:
                list_num.remove(i + (i//1000) + ((i%1000)//100) + ((i%1000%100)//10) + (i%10))
            except ValueError:
                continue
    for _ in list_num:
        print(_)
    return None

self_num(list_num)
