def solution(my_string):
    # result = ''
    # for x in my_string:
    #     if not x in 'aeiou':
    #         result += x
    cond = 'aeiou'
    result = ''
    
    for x in my_string:
        if x not in cond:
            result += x
    return result