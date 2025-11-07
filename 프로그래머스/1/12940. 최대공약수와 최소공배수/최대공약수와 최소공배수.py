import math
def solution(n, m):
    result = []
    gcd = math.gcd(n, m)
    result = [gcd, int(n * m / gcd)]
    return result