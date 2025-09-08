def solution(arr):
    stk = []
    for idx in range(len(arr)):
        if not stk:
            stk.append(arr[idx])
        else:
            if stk[-1] == arr[idx]:
                stk.pop()
                idx += 1
            else:
                stk.append(arr[idx])

    if not stk:
        stk.append(-1)
    return stk