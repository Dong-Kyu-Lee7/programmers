def solution(box, n):
    result = 1
    for x in range(len(box)):
        result *= box[x] // n
    return result