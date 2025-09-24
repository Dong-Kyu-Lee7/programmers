def solution(n):
    result = 0
    for x in range(n+1):
        if x % 2 == 0:
            result += x
    return result