def solution(A):
    n = len(A)
    s = (n+1)*(n+2)//2
    if n==0 or min(A) ==2:
        return 1
    elif s == sum(A):
        return n+1
    else :
        return s - sum(A)


