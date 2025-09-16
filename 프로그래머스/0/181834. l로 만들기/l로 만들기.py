def solution(myString):
    result = ''
    for x in range(len(myString)):
        if myString[x] < 'l':
            result += 'l'
        else:
            result += myString[x]
    return result