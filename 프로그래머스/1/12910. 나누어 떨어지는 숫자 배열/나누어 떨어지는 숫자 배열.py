def solution(arr, divisor):
    result = []
    for x in arr:
        if x % divisor == 0:
            result.append(x)
    if len(result) == 0:
        result = [-1]
    result = sorted(result)
    return result