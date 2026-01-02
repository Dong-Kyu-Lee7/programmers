def solution(a, b):
    cond1 = int(str(a) + str(b))
    cond2 = 2 * a * b
    
    # if cond2 > cond1:
    #     answer = cond2
    # else:
    #     answer = cond1
    if cond1 > cond2:
        result = cond1
    elif cond2 > cond1:
        result = cond2
    elif cond1 == cond2:
        result = cond1
        
    return result