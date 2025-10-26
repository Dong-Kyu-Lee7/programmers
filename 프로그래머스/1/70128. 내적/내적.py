def solution(a, b):
    result = 0
    for x in range(len(a)):
        result += a[x] * b[x]
    return result