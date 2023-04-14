count_1=int(input())
for _ in range(1,count_1+1):
    index_1,word_1=input().split()
    word_2=word_1.strip(word_1[int(index_1)-1])
    print(word_2)