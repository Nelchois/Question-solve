import sys
case = int(sys.stdin.readline())
def recursion(s, l, r):
    if l >= r: return [1, l]
    elif s[l] != s[r]: return [0, l]
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for i in range(case):
    word = sys.stdin.readline().rstrip()
    print(isPalindrome(word)[0], isPalindrome(word)[1]+1, sep= ' ')
