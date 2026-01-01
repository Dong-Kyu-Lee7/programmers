import string

def solution(my_string):
    # low_str = string.ascii_letters
    # result = 0
    # for x in my_string:
    #     if not x in low_str:
    #         result +=int(x)
            
    cond = string.ascii_letters
    result = 0
    for x in my_string:
        if x not in cond:
            result += int(x)
    return result