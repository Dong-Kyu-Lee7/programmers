def solution(before, after):
    result = 0
    if sorted(before) == sorted(after):
        result = 1
    return result