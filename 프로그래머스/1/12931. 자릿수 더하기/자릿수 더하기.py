def solution(n):
    result = 0
    # int(str(N)[0]) + int(str(N)[1])
    for x in str(n):
        result += int(x)

    return result