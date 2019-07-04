def solution(A):
    le = len(A)
    rst1 = []
    rst2 = []
    for i in range(le-1):
        t =(A[i]+A[i+1])/2
        rst1.append(t)
    if le >2:
        for i in range(le-2):
            t = (A[i]+A[i+1]+A[i+2])/3
            rst2.append(t)
        if min(rst1)<=min(rst2):
            return rst1.index(min(rst1))
        else:
            return rst2.index(min(rst2))
    else:
        return rst1.index(min(rst1))
