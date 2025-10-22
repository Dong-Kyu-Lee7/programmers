def solution(a, b):
    result = 0
    if a <= b:
        for x in range(a,b+1):
            result += x
    else:
        for x in range(b,a+1):
            result += x
    return result