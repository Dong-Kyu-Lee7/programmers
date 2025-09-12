def solution(rank, attendance):
    tmp = []
    for idx,val in enumerate(rank):
        if attendance[idx] == 1:
            tmp.append(rank[idx]) # [7, 2, 5, 4]
    tmp.sort(); # [2, 4, 5, 7]

    a,b,c = 0,0,0
    result = 0
    for idx, val in enumerate(rank):
        if val == tmp[0]:
            a = idx
        elif val == tmp[1]:
            b = idx
        elif val == tmp[2]:
            c = idx

    result = 10000 * a + 100 * b + c
    return result