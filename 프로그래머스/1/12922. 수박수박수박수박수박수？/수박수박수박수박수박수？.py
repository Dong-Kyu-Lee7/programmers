def solution(n):
    result = ''
    for x in range(1,n+1):
        if x % 2 != 0:
            result += '수'
        else:
            result += '박'
    return result