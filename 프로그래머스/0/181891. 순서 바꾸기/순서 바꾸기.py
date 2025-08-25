def solution(num_list, n):
    result = num_list[n:] # [1,6]
    result.extend(num_list[:n])
    return result