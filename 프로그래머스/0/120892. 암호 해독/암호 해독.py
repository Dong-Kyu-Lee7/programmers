def solution(cipher, code):
    result = ''
    for x in range(1,len(cipher)+1):
        if x % code == 0:
            result += cipher[x-1]
    return result