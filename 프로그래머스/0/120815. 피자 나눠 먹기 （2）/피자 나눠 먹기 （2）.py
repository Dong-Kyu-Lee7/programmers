def solution(n):
    result = 0
    p = 6
    
    for x in range(1, p * n +1):
        if (p * x) % n == 0:
            result = x
            break
    return result