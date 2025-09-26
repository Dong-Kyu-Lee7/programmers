def solution(numbers):
    result = 0
    numbers.sort()
    result = numbers[-2] * numbers[-1]
    return result