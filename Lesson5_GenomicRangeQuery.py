def solution(S,P,Q):
    M = len(P)
    ans = []
    for i in range(M):
        p = P[i]
        q = Q[i]
        if 'A' in S[p:q+1]:
            ans.append(1)
        elif 'C' in S[p:q+1]:
            ans.append(2)
        elif 'G' in S[p:q+1]:
            ans.append(3)
        else:
            ans.append(4)
    return ans

x = solution('CAGCCTA',[2,5,0],[4,5,6])
print(x)

# solution2 first trial / time complexity O(N*M) / score 62%
def solution2(S,P,Q):
    A=[0]*100001
    C=[0]*100001
    G=[0]*100001
    T=[0]*100001
    for i,v in enumerate(S):
        if v=='A':
            A[i]=1
        elif v=='C':
            C[i]=1
        elif v=='G':
            G[i]=1
        else:
            T[i]=1
    M = len(P)
    ans = [0]*M
    for j in range(M):
        p=P[j]
        q=Q[j]
        if 1 in A[p:q+1] :
            ans[j]=1
        elif 1 in C[p:q+1]:
            ans[j] = 2
        elif 1 in G[p:q+1]:
            ans[j] = 3
        else:
            ans[j] = 4
    return ans