def solution(arr1, arr2):
    result = 0

    if len(arr1) != len(arr2):
        if len(arr1) > len(arr2):
            result = 1
        else:
            result = -1
    else:
        if sum(arr1) == sum(arr2):
                result = 0
        else:
            if sum(arr1) > sum(arr2):
                result = 1
            else:
                result = -1
    return result