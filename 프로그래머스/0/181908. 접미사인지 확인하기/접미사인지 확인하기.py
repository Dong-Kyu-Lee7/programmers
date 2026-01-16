def solution(my_string, is_suffix):
    check_list = []

    for x in range(len(my_string)):
        check_list.append(my_string[x:])
        if is_suffix in check_list:
            result = 1
        else:
            result = 0
    return result