def solution(strArr):
    result = []
    tmp = []
    for x in strArr:
        tmp.append(len(x))

    for y in range(1,max(tmp)+1):
        result.append(tmp.count(y))
    return max(result)