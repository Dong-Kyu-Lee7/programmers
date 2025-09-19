def solution(array):
    result = 0
    array = sorted(array)
    result = array[len(array) // 2]
    return result