def solution(numlist, n):
    result = []
    tmp = []

    for x in numlist:
        tmp.append((abs(n - x), -x)) # 3,2,1,0,1,2

    tmp.sort()
    # print(tmp)
    for f,s in tmp:
        result.append(-s)

    return result