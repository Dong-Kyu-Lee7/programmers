def solution(strArr):
    result = []
    for x in strArr:
        if 'ad' not in x:
            result.append(x)
    return result