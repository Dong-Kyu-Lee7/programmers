def solution(price):
    ## result = 0
    # if price >= 100000 and price < 300000:
    #     result = 0.95 * price
    # elif price >= 300000 and price < 500000:
    #     result = 0.9 * price
    # elif price >= 500000:
    #     result = 0.8 * price
    # elif price < 100000:
    #     result = price
    
    cond1 = 100000
    cond2 = 300000
    cond3 = 500000
    
    if price >= cond1 and price < cond2:
        result = 0.95 * price
    elif price >= cond2 and price < cond3:
        result = 0.9 * price
    elif price >= cond3:
        result = 0.8 * price
    else:
        result = price
    return int(result)