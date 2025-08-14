def solution(q, r, code):
    result = ''
    
    for x,y in enumerate(code):
        # print(x,y)
        if x % q == r:
            # print(y)
            result += y
    return result