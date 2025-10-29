def solution(s):
    result = True
    tmp = []
    for x in s:
        if x == '(':
            tmp.append(x)
        else: # ')'인 경우
            if tmp == []:
                result = False
            else: # '(' 존재한 경우
                tmp.pop()

    if tmp != []:
        result = False
    return result