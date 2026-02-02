def solution(num_list):
#     result = 0
#     if len(num_list) >= 11:
#         for x in num_list:
#             result += x

#     elif len(num_list) <= 10:
#         result += 1
#         for x in num_list:
#             result *= x 
    result = 0
    if len(num_list) >= 11:
        for x in num_list:
            result += x

    else:
        result = 1
        for x in num_list:
            result *= x
    return result