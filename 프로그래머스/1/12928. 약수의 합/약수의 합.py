def solution(n):
    result = 0
    tmp = []
    for x in range(1,n+1):
        if n % x == 0:
            tmp.append(x)
    result = sum(tmp)
    return result