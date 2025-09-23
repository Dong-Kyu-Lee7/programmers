def solution(num_list):
    result = []
    even_lst = []
    odd_lst = []
    for x in num_list:
        if x % 2 == 0:
            even_lst.append(x)
        else:
            odd_lst.append(x)

    result.append(len(even_lst))
    result.append(len(odd_lst))
    return result