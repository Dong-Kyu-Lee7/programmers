def solution(n):
    result = []
    d = 2
    while d <= n:
        if n % d == 0:
            n = n // d
            if d not in result:
                result.append(d)
        else:
            d += 1
    return result