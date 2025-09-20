def solution(n):
    result = []
    for x in range(n+1):
        if x % 2 != 0:
            result.append(x)
    return result