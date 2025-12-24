def solution(n):
#     p = 7

#     if n % p == 0:
#         result = n // p
#     else:
#         result = (n // p) + 1
    
    result = 0
    
    if n % 7 == 0:
        result = n // 7
    else:
        result = (n // 7) + 1
    return result