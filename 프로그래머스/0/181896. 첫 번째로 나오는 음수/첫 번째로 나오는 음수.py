def solution(num_list):
    for id,val in enumerate(num_list):
        if val < 0:
            return id
    return -1