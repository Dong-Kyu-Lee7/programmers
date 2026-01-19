def solution(my_string, is_prefix):
    list_string = []
    
    result = 0
    for x in range(len(my_string)):
        list_string.append(my_string[:x+1])
        if is_prefix in list_string:
            result = 1
    
    return result
