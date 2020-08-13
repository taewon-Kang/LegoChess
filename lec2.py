a, b=map(int, input().split())
words=[str(input()) for _ in range(a)]
sums=list()
cnt=0
cnt2=0

for i in range(a):
    words[i]=list(map(int, list(str(words[i]))))
    
for i in range(a-1):
    for j in range(i, a):
        temp=0
        for k in range(b):
            if words[i][k]+words[j][k] >= 1:
                temp+=1
        if temp>=cnt:
            cnt=temp
            sums.append(cnt)

for i in range(len(sums)):
    if sums[i]==cnt:
        cnt2+=1
            
print(cnt)
print(cnt2)

