def solution(rsp):
    result = ''
    for x in rsp:
        if x == '0':
            result += '5'
        elif x == '2':
            result += '0'
        elif x == '5':
            result += '2'
    return result