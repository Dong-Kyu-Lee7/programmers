def solution(order):
    result = 0
    tmp = []

    for x in range(len(order)):
        if order[x] == 'anything':
            order[x] = order[x].replace('anything', 'americano')
            # print(order)
        if 'americano' not in order[x]: # 라떼
            result += 5000
            # print(x)
        #     # print(result)
        else:
            result += 4500
    return result