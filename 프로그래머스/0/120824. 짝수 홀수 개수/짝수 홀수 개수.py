def solution(num_list):
    result = []
    even_lst = []
    odd_lst = []
    for i in num_list:
        if i % 2 == 0:
            even_lst.append(i)
        else:
            odd_lst.append(i)

    result.append(len(even_lst))
    result.append(len(odd_lst))
    return result