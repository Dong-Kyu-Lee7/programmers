def solution(myStr):
    result = []
    cond = myStr.replace('a', ' ').replace('b', ' ').replace('c',' ')

    result = cond.split()
    if not result:
        result.append('EMPTY')
    return result