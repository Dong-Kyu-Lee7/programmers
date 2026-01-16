def solution(a, b):
#     cond1 = str(a) + str(b)
#     cond2 = str(b) + str(a)
    
#     if int(cond1) > int(cond2):
#         answer = int(cond1)
#     else:
#         answer = int(cond2)
    cond1 = int(str(a) + str(b))
    cond2 = int(str(b) + str(a))

    result = cond2
    if cond1 > cond2:
        result = cond1
    return result