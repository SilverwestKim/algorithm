from itertools import combinations
N = int(input())
A=[[0]]*N
ans = []
for j in range(N):
    tmp = str.split(input()," ")
    A[j] = [int(i) for i in tmp]

b = list(combinations(range(N),N//2))
b = b[:len(b)//2]

for k in b:
    l = list(range(N))
    temp1=0
    temp2=0
    for p in k:
        for q in k:
            temp1 += A[p][q]
        l.remove(p)

    for r in l:
        for s in l:
            temp2 +=A[r][s]
    tmp = abs(temp1-temp2)
    ans.append(tmp)

print(min(ans))