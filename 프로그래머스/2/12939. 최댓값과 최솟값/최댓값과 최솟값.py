def solution(s):
    result = ''
    tmp = []
    for x in s.split():
        tmp.append(int(x))
    result = str(min(tmp)) + ' ' + str(max(tmp))
    return result