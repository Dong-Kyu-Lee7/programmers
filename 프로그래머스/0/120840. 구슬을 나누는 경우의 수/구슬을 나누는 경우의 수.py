def solution(balls, share):
    result = 0
    n = 1
    for x in range(share):
        n *= (balls - x)
    
    denom = 1
    for x in range(1,share+1):
        denom *= x
    
    result = n // denom
    return result