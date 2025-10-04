def solution(n):
    if n ** (1/2) != int(n ** (1/2)):
        result = 2
    else:
        result = 1
    return result