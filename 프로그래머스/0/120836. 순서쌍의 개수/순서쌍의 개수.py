def solution(n):
    result = 0
    for x in range(1,n+1):
        if n % x == 0:
            result +=1
    return result