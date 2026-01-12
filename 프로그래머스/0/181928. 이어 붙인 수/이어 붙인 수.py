def solution(num_list):
    # answer = 0
    odd_num = ''
    even_num = ''
    for x in num_list:
        if x % 2 == 1: # odd
            odd_num += str(x)
        else:
            even_num += str(x)
    
    result = int(odd_num) + int(even_num)
    return result