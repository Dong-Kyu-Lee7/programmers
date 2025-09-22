def solution(money):
    result = []
    if money % 5500 == 0:
        result.append(money // 5500)
        result.append(money % 5500)
    else:
        result.append(money // 5500)
        result.append(money % 5500)
    return result