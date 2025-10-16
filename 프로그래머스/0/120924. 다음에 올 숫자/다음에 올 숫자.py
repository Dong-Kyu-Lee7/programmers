def solution(common):
    result = 0
    f,s,t = common[:3]
    if s - f == t - s:
        result = common[-1] + (s - f)
    elif s // f == t // s:
        result = common[-1] * (s // f)
    return result