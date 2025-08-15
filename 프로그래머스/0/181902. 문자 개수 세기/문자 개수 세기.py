def solution(my_string):
    result = []

    for x in 'abcdefghijklmnopqrstuvwxyz'.upper()+'abcdefghijklmnopqrstuvwxyz':
        # print(x.upper())
        result.append(my_string.count(x))
    return result