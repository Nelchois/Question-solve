A = [1, 4, 2] 
B = [5, 4, 4]
ans = [0]
def solution():
    for i in range(len(A)):
        ans[0] += A.pop(A.index(max(A))) * B.pop(B.index(min(B)))
    return
solution()
print(ans)