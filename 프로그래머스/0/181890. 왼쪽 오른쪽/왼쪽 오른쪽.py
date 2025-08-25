def solution(str_list):
    result = []

    for x in range(len(str_list)):
        if str_list[x] == 'l':
            result = str_list[:x]
            break
        elif str_list[x] == 'r':
            result = str_list[x+1:]
            break
    return result