def solution(my_string, alp):
    result = ''
    for x in my_string:
        if x == alp:
            result += x.upper()
        else:
            result += x

        # result += x
    return result