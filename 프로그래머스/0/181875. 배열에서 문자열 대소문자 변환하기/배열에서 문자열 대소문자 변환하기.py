def solution(strArr):
    result = []
    for x in range(len(strArr)):
        if x % 2 == 0: # 짝수
            result.append(strArr[x].lower())
        else:
            result.append(strArr[x].upper())
    return result