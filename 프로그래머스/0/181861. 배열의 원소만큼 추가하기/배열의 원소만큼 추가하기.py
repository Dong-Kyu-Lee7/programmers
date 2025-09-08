def solution(arr):
    result = []
    for x in arr:
        for y in range(x):
            result.append(x)
    return result