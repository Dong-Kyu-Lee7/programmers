def solution(binomial):
    result = 0
    a,op,b = binomial.split()
    if op == '+':
        result = int(a) + int(b)
    elif op == '-':
        result = int(a) - int(b)
    else:
        result = int(a) * int(b)
    return result