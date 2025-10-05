def solution(my_str, n):
    result = []
    for x in range(0, len(my_str),n):
        result.append(my_str[x:n+x])
    return result