def solution(cipher, code):
    result = ''
    for i in range(1,len(cipher)+1):
        if i % code == 0:
            result += cipher[i-1] # 인덱스 '0'부터 시작해서
    return result