def solution(price):
    # result = 0
    if price >= 100000 and price < 300000:
        result = 0.95 * price
    elif price >= 300000 and price < 500000:
        result = 0.9 * price
    elif price >= 500000:
        result = 0.8 * price
    elif price < 100000:
        result = price
    return int(result)