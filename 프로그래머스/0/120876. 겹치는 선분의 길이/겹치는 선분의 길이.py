def solution(lines):
    tmp = []
    for x in lines:
        tmp.append(set(range(min(x), max(x)))) # tmp: [{0}, {2, 3, 4}, {3, 4, 5, 6, 7, 8}]
    result = len(tmp[0] & tmp[1] | tmp[0] & tmp[2] | tmp[1] & tmp[2])
    # print(tmp)
    # print(result)
    return result