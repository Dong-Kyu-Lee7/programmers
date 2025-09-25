def solution(num_list, n):
    result = []
    for x in range(len(num_list) // n): # 0~3
        result.append(num_list[n*x:n*(x+1)])
    return result