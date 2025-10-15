def solution(chicken):
    result = 0
    while chicken >= 10:
        q = chicken // 10
        r = chicken % 10
        chicken = q + r
        result += q
    return result