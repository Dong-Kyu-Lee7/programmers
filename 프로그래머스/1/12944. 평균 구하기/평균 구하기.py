def solution(arr):
    result = 0
    for x in arr:
        result += x
    result = result / len(arr)
    return result