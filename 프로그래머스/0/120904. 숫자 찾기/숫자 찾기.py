def solution(num, k):
    result = -1
    
    for idx,val in enumerate(str(num)):
        if val == str(k):
            result = idx + 1
            break
    return result