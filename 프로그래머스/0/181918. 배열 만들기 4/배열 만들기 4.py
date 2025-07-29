def solution(arr):
    stk = []
    i = 0

    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i]) # i = 1, arr[i] = 4, stk = [1]
            i += 1
        elif len(stk) != 0 and (stk[-1] < arr[i]):
            stk.append(arr[i])
            i += 1 # # i = 2, arr[i] = 2, stk = [1,4]
        elif len(stk) != 0 and (stk[-1] >= arr[i]):
            stk.pop()
    return stk