def solution(numbers):
    result = 0
    tmp = []
    for x in range(10):
        if x not in numbers:
            tmp.append(x)
    result = sum(tmp)
    return result