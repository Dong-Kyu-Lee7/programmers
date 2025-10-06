def solution(polynomial):
    x_sum = 0
    const = 0
    result = ''
    for x in polynomial.split(' + '):
        if 'x' in x:
            if 'x' == x:
                x_sum += 1
            else:
                x_sum += int(x[:-1]) # 'x'의 계수값
        else:
            const += int(x)

    if const == 0:
        if x_sum != 1:
            result = f'{x_sum}x'
        else:
            result = 'x'
    elif x_sum == 0:
        result = f'{const}'
    else:
        if x_sum != 1:
            result = f'{x_sum}x + {const}'
        else:
            result = f'x + {const}'
    return result