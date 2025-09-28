import string

def solution(my_string):
    low_str = string.ascii_lowercase
    result = []
    for x in my_string:
        if not x in low_str:
            result.append(int(x))
    result = sorted(result)
    return result