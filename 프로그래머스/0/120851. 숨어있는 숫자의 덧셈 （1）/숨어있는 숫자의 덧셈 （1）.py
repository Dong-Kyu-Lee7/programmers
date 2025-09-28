import string

def solution(my_string):
    low_str = string.ascii_letters
    result = 0
    for x in my_string:
        if not x in low_str:
            result +=int(x)
    return result