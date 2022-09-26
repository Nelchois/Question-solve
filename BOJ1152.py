import sys
word_list = list(sys.stdin.readline().lstrip().rstrip().split(' '))

if word_list[0] == '':
    print(0)
else:
    print(len(word_list))
