def solution(arr):
    r = len(arr) # 행
    c = len(arr[0]) # 열

    if r > c:
        for x in range(r):
            for y in range(r-c):
                arr[x].append(0)
    else:
        for x in range(c-r):
            arr.append([0] * c)
    return arr