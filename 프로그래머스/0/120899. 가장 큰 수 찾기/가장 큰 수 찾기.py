def solution(array):
    result = []
    tmp = max(array)
    result = [tmp, array.index(tmp)]
    return result