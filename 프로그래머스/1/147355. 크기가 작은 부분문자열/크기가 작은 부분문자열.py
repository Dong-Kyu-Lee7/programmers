def solution(t, p):
    p_len = len(p)
    p_val = int(p)
    count = 0
    
    # t에서 p와 같은 길이의 부분문자열 추출
    for i in range(len(t) - p_len + 1):
        sub_str = t[i:i + p_len]
        if int(sub_str) <= p_val:
            count += 1
            
    return count