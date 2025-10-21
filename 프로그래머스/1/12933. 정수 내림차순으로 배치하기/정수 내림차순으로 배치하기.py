def solution(n):
    n = str(n)
    result = 0
    tmp = []
    for x in n:
        tmp.append(x)

    result = int(''.join(sorted(tmp, reverse = True)))
    return result