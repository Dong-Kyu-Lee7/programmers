def solution(my_string, indices):
    result = ''

    for x in range(len(my_string)):
        if x not in indices:
            result += my_string[x]
    return result