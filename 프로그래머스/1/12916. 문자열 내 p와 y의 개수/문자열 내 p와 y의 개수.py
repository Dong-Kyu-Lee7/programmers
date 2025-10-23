def solution(s):
    s = s.lower()
    s_cnt = s.count('p')
    y_cnt = s.count('y')

    if s_cnt == y_cnt:
        result = True
    else:
        result = False

    return result