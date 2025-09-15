def solution(a, b):
    result = 0
    if (a % 2 != 0) and (b % 2 != 0):
        result = (a ** 2) + (b ** 2)
    elif (a % 2 != 0) or (b % 2 != 0):
        result = 2 * (a+b)
    else:
        result = abs(a - b)
    return result