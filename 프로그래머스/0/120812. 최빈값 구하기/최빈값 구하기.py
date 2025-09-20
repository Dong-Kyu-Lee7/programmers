from collections import Counter
def solution(array):
    result = 0
    mode = []
    arr_cnt = Counter(array)
    arr_max = max(arr_cnt.values())

    for idx, val in arr_cnt.items():
        if val == arr_max:
            mode.append(idx)
    if len(mode) == 1:
        result = mode[0]
    else:
        result = -1
    return result