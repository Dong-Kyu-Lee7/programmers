def solution(arr):
    result = []

    for id,val in enumerate(arr):
        if val == 2:
            result.append(id)

    if len(result) > 0:
        result = arr[result[0]:result[-1]+1]
    else:
        result = [-1]
    return result