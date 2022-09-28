import sys
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = sys.stdin.readline().rstrip()
low_word = word.lower()
number = []
for i in range(len(alpha)):
    num = low_word.count(alpha[i])
    number.append(num)
if number.count(max(number)) > 1:
    print('?')
else:
    print(alpha[number.index(max(number))].upper())
