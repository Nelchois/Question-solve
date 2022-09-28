import sys
word = sys.stdin.readline().rstrip()
try:
    word = word.replace('c=', 'c')
except:
    pass
try:
    word = word.replace('c-', 'c')
except:
    pass
try:
    word = word.replace('dz=', 'd')
except:
    pass
try:
    word = word.replace('d-', 'd')
except:
    pass
try:    
    word = word.replace('s=', 's')
except:
    pass
try:
    word = word.replace('z=', 'z')
except:
    pass
try:
    word = word.replace('lj', 'l')
except:
    pass
try:
    word = word.replace('nj', 'n')
except:
    pass
print(len(word))
