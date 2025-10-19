def solution(n):
    n = list(str(n))
    result = []
    
    for x in n[::-1]:
        result.append(int(x))

    return result