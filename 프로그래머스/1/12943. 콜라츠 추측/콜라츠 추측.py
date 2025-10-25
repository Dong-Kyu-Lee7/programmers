def solution(num):
    result_cnt = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        
        result_cnt += 1

        if result_cnt == 500:
            return -1
    return result_cnt