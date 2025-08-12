def solution(my_string, is_prefix):
    result = []
    for x in range(len(my_string)):
        result.append(my_string[:x])
        if is_prefix in result:
            answer = 1
        else:
            answer = 0
    return answer