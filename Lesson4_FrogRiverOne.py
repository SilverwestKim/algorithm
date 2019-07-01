def solution(X, A):
    check = [0] * X
    check_sum = 0
    for i, v in enumerate(range(len(A))):
        if check[v-1] ==0:
            check[v-1]=1
            if check_sum ==X:
                return i
    return -1


#solution2 score 53/100 (time out error)
def solution(X, A):
    rst = 0
    whe = [False]*X
    for i,v in enumerate(A):
        if whe[v-1] == False:
            whe[v-1]=True
            rst +=1
            if rst ==X:
                return i
    return -1