def solution(price, money, count):
    result = 0
    for x in range(1,count+1):
        result += price * x

    if result - money <= 0:
        result = 0
    else:
        result = result - money

    return result