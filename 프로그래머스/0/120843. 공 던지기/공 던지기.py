def solution(numbers, k):
    result = 0
    result = numbers[2*(k-1) % len(numbers)]
    return result