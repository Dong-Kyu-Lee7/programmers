def solution(a, b):
    cond1 = int(str(a) + str(b))
    cond2 = 2 * a * b
    
    if cond2 > cond1:
        answer = cond2
    else:
        answer = cond1
        
    return answer