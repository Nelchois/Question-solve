word=input()
CAM_l=[]
if 2<len(word)<101:
    for i in range(1,10):
        CAM_l.append("CAMBRIDGE"[i-1:i])
    for j in CAM_l:
        word=word.replace(j,"")
print(word)