def solution(sides):
    result = 0
    max_num = max(sides)
    sides.remove(max_num)
    sum_sides = sum(sides)
    if max_num < sum_sides:
        result = 1
    else:
        result = 2
    return result