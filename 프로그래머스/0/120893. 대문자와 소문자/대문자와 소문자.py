def solution(my_string):
    result = ''
    for x in my_string:
        if x.islower():
            result += x.upper()
        else:
            result += x.lower()
    return result