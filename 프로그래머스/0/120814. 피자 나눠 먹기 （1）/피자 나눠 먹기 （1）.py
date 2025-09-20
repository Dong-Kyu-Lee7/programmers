def solution(n):
    p = 7

    if n % p == 0:
        result = n // p
    else:
        result = (n // p) + 1
    return result