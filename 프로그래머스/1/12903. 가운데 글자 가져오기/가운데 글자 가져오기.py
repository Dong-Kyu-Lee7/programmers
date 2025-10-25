def solution(s):
    result = ''
    len_s = len(s)
    if len_s % 2 != 0: # 홀
        result = s[(len_s // 2)]
    else: # 짝
        result = s[(len_s // 2)-1:(len_s // 2) + 1]
    return result