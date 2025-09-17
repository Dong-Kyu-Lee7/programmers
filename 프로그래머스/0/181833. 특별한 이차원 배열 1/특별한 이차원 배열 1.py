def solution(n):
    result = []

    for x in range(n):
        row = []
        for y in range(n):
            if x == y:
                row.append(1)
            else:
                row.append(0)
        result.append(row)
    return result