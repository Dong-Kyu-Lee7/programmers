def solution(score):
    result = []
    tmp = []
    for s in score:
        tmp.append((s[0]+ s[1]) / len(s))

    sort_tmp =sorted(tmp, reverse=True) # [75, 70, 65, 55]

    for x in tmp:
        result.append(sort_tmp.index(x) + 1)
    return result