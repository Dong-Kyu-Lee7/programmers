def solution(number, n, m):
    answer = int((number % n == 0) & (number % m == 0))
    return answer