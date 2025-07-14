def solution(num_list):
    
    # last_num = int(num_list[-1])
    # pre_num = int(num_list[-2])

    if int(num_list[-1]) > int(num_list[-2]):
        num_list.append(int(num_list[-1]) - int(num_list[-2]))
    else:
        num_list.append(int(num_list[-1]) * 2)
    return num_list