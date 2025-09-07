def solution(myString, pat):
    result = 0
    cond = myString.replace('A', 'a').replace('B', 'A').replace('a', 'B')

    if pat in cond:
        result = 1
    else:
        result = 0
    return result