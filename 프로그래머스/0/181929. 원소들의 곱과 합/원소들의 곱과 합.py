def solution(num_list):
    answer = 0
    total_sum = 0
    total_multi = 1
    for i in num_list:
        total_sum += i
        total_multi = total_multi * i
        
        if total_sum ** 2 > total_multi:
            answer = 1
        else:
            answer = 0
    return answer