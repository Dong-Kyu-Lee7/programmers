def solution(my_string, n):
    result = ''
    for x in my_string:
        result = result + (x * n)
    return result