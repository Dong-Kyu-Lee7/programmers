def solution(my_string):
    result = ''
    for x in my_string[::-1]:
        result += x
    return result