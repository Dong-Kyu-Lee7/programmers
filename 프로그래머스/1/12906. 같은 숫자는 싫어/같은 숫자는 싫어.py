def solution(arr):
    result = []
    for x in arr:
        if result and result[-1] == x:
            continue
        else:
            result.append(x)
    return result