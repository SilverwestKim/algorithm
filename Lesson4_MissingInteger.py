def solution(A):
    if max(A)<=0:
        return 1
    else :
        T = [0]*1000001
        for k in A:
            if k>0:
                T[k]=1
        T.pop(0)
        i=T.index(0)+1
        return i
