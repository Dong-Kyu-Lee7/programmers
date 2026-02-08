def solution(str1, str2):
#     answer = ""
#     for i in range(0, len(str1)):
#         answer = answer + str1[i] + str2[i]
    
    result = ''

    for x in range(len(str1)):
        result += str1[x] + str2[x]

    return result