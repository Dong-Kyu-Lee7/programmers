def solution(my_string):
    result = 0
    tmp = ''
    for x in my_string:
        if x.isdigit():
            tmp += x
        else:
            tmp += " "


    for x in tmp.split():
        result += int(x)
    return result