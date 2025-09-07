def solution(rny_string):
    result = ''
    if 'm' in rny_string:
        result = rny_string.replace('m', 'rn')
    else:
        result =rny_string
    return result