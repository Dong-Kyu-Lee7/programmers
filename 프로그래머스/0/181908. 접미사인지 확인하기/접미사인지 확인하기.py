def solution(my_string, is_suffix):
    result = []

    for x in range(len(my_string)):
        result.append(my_string[x:])
        if is_suffix in result:
            answer = 1
        else:
            answer = 0
    return answer