def solution(numbers):
    result = 0
    for x in numbers:
        result += x
    result = result / len(numbers)
    return result