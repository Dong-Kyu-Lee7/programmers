def solution(n):
    result = 1
    num = 1
    for x in range(1,11):
        num *= x
        if num <= n:
            result = x
    return result