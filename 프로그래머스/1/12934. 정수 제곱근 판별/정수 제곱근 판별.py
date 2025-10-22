def solution(n):
    result = 0
    num = n ** (1/2)
    if num  % 1 == 0:
        result = (num+1) ** 2
    else:
        result = -1
    return result