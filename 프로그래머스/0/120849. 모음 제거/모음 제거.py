def solution(my_string):
    result = ''
    for x in my_string:
        if not x in 'aeiou':
            result += x
    return result