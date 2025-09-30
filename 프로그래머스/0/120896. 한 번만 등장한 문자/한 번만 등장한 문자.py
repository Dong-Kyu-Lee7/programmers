def solution(s):
    result = ''
    for x in s:
        if s.count(x) == 1:
            result += x
    result = ''.join(sorted(result))
    return result