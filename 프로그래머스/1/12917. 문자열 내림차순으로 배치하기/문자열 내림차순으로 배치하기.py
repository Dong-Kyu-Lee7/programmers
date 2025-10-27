def solution(s):
    result = ''
    new_s = sorted(s, reverse = True)
    result = ''.join(new_s)
    return result