def solution(myString):
    # result = ''
    # for x in myString:
    #     if x == 'a' or x == 'A':
    #         x = x.upper()
    #     else:
    #         x = x.lower()
    #     result += x
        
    result = ''
    for x in myString:
        if x == 'a':
            x = x.upper()
        elif x != 'A':
            x = x.lower()
        result += x
    return result