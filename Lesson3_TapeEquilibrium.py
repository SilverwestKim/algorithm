def solution(A):
    ans = []
    asum= []
    n = len(A)
    if n ==2:
        return abs(A[0]-A[1])
    s=0
    for p in A:
        s +=p
        asum.append(s)
    for k in asum:
        ans.append(abs(2*k-asum[-1]))
    return min(ans)