def solution(arr, flag):
    X = []
    for idx, val in enumerate(flag):
        if val:
            for i in range(0,arr[idx] * 2):
                X.append(arr[idx])
        else:
            for i in range(0, arr[idx]):
                X.pop()
    return X