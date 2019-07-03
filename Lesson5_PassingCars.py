def solution(A):
    one_cnt = A.count(1)
    x=0
    for i in A:
        if i==0:
            x+=one_cnt
        else:
            one_cnt-=1
    if x>1000000000:
        return -1
    else :
        return x