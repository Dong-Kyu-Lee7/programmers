def solution(bin1, bin2):
    result = ''
    bin1 = '0b' + bin1
    bin2 = '0b' + bin2
    a,b = int(bin1, 2), int(bin2,2)
    tmp = a + b
    result = bin(tmp)[2:]
    result
    return result