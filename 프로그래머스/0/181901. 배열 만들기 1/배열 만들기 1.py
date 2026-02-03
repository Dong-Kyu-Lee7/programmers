def solution(n, k):
    result = []

    for x in range(1,n+1):
        if x % k == 0:
            result.append(x)
    return sorted(result)