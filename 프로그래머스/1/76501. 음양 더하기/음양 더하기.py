def solution(absolutes, signs):
    converted = []
    for s in signs:
        converted.append(str(s).lower())

    signs = converted
    result = 0
    tmp = []
    for x in range(len(signs)): # 0,1,2
        if signs[x] == 'true':
            tmp.append(absolutes[x])
        elif signs[x] == 'false':
            tmp.append(-absolutes[x])

    result = sum(tmp)
    return result