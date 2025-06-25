def solution(my_string, overwrite_string, s):
    
    answer = f'{my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]}'
    return answer

# a = solution()
# print(a)