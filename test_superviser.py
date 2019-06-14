N = int(input())
A = str.split(input()," ")
for i in range(len(A)):
    A[i] = int(A[i])
k=str.split(input()," ")
b = int(k[0]); c = int(k[1])

cnt = []
for j in A:
    tmp = j-b
    if tmp>0 :
        if tmp%c ==0:
            cnt.append(tmp//c +1)
        else :
            cnt.append(tmp//c +2)
    else:
        cnt.append(1)

print(sum(cnt))






