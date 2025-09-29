def solution(order):
    result = 0
    for x in str(order):
        if x in '369':
            result += 1
    return result