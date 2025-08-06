def solution(my_strings, parts):
    result = ''

    for inx,val in enumerate(parts): # s = 0,1,3,7 e = 4,2,5,7
        result += my_strings[inx][val[0]:val[1]+1]
    return result