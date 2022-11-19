import sys 
number = 666
movie_number_list = []
movie = int(sys.stdin.readline())
while len(movie_number_list) < movie:
    if '666' in str(number):
        movie_number_list.append(number)
    number += 1
print(movie_number_list[movie - 1])
