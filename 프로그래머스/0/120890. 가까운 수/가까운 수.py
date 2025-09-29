def solution(array, n):
    result = 0
    array.sort()
    abs_result = []
    for x in range(len(array)):
        abs_result.append(abs(n - array[x]))

    result = array[abs_result.index(min(abs_result))]
    return result