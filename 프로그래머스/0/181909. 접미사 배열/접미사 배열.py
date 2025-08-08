def solution(my_string):
    result = []

    for x in range(len(my_string)):
        # print(x)
        result.append(my_string[x:])
    
    result = sorted(result)
    
    return result