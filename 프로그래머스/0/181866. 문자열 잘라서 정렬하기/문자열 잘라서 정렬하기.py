def solution(myString):
    result = []
    for x in myString.split('x'):
        if x != '':
            result.append(x)
    return sorted(result)