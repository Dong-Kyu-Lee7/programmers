def solution(my_string, alp):
    result = ''
    for x in my_string:
        if x == alp:
            x = x.upper()
        else:
            x = x

        result += x
    return result