def solution(a, b):
    result = 0

    for i in range(b,0,-1):
        if a%i == 0 and b%i == 0:
            d=i # d 최대공약수
            break
    a = (a // d)
    b = (b // d)

    num = []
    d = 2
    while d <= b:
        if b % d == 0:
            b = b // d
            num.append(d)
        else:
            d += 1
    # print(num)

    all_true = True
    for x in num:
        if x not in [2,5]:
            all_true = False

    if all_true:    
        result = 1
    else:
        result = 2
    return result