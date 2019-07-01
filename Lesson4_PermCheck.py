def solution(A):
    A.sort()
    M = max(A)
    if A[-1]>100000:
        return 0
    if len(A)==1:
        if A[0]==1:
            return 1
        else:
            return 0
    else :
        l = list(range(1,M+1))
        if A==l:
            return 1
        else :
            return 0