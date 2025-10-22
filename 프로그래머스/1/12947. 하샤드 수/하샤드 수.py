def solution(x):
    result = False
    tmp = []
    for i in str(x):
        tmp.append(int(i))

    h = sum(tmp)

    if x % h == 0:
        result = True
    return result