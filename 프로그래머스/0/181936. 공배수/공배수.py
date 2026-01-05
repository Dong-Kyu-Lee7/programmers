def solution(number, n, m):
    # answer = int((number % n == 0) & (number % m == 0))
    
    result = 0
    if (number % n == 0) & (number % m == 0):
        result = 1
    return result