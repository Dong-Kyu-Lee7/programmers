def solution(my_string, letter):
    result = ''
    for x in my_string:
        if x != letter:
            result += x
    return result