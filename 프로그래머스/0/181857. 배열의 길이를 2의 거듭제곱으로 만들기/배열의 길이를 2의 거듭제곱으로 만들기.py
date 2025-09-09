def solution(arr):
    result = []
    for x in range(11):
        result.append(2**x)
    while len(arr) not in result:
        arr.append(0)
    return arr