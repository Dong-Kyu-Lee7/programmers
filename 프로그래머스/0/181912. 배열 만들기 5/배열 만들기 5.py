def solution(intStrs, k, s, l):
    result = []

    for x in intStrs:
        if int(x[s:s+l]) > k:
            result.append(int(x[s:s+l]))
    return result