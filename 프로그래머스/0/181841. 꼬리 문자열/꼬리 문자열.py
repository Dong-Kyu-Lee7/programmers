def solution(str_list, ex):
    result = ''
    for x in str_list:
        if ex not in x:
            result += x
    return result