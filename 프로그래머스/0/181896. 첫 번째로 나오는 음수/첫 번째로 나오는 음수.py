def solution(num_list):
    # for id,val in enumerate(num_list):
    #     if val < 0:
    #         return id
    
    result = -1
    
    for id, val in enumerate(num_list):
        if val < 0:
            result = id
            break
    return result