def solution(n, control):
#     answer = n
    
#     for i in control:
#         if i == 'w':
#             answer += 1
            
#         elif i == 's':
#             answer -= 1
            
#         elif i == 'd':
#             answer += 10
#         else:
#             answer -= 10
    for x in control:
        if x == 'w':
            n += 1
        elif x == 's':
            n -= 1
        elif x == 'd':
            n += 10
        elif x == 'a':
            n -= 10
    return n