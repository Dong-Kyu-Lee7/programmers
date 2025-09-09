def solution(arr, k):
    result = []

    for x in arr:
        if x not in result:
            result.append(x)
        if len(result) == k:
            break

    if len(result) < k:
        result.extend([-1] * (k-len(result)))
    return result