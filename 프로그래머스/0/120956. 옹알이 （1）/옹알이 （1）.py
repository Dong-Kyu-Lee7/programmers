def solution(babbling):
    result = 0
    cond = ["aya", "ye", "woo", "ma"]
    for x in babbling:
        tmp = ''
        for y in range(len(x)):
            tmp += x[y]
            # print(tmp)
            if tmp in cond:
                # print(tmp)
                tmp = ''

        if tmp == '':
            result += 1
    return result