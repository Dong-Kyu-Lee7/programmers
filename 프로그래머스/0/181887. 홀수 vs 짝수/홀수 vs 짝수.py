def solution(num_list):
    even_num = 0
    odd_num = 0

    for x in range(len(num_list)):
        if x % 2 == 0:
            odd_num += num_list[x]
        else:
            even_num += num_list[x] # num_list[x+1] -> 2,1,6

    if odd_num > even_num:
        result = odd_num
    else:
        result = even_num
    return result