def solution(a, b, c, d):
    answer = 0
    lst = [a,b,c,d]
    counts = [lst.count(x) for x in lst]
            
    if max(counts) == 4:
        answer += 1111 * lst[0]
    elif max(counts) == 3:
        answer += (10*lst[counts.index(3)]+lst[counts.index(1)])**2
    elif max(counts) == 2:
        if min(counts) == 2:
            answer += (max(lst) + min(lst)) * (max(lst) - min(lst))
        else:
            p = lst[counts.index(2)]
            return (a * b * c * d) / p**2
    else:
        answer = min(lst)
        
    return answer