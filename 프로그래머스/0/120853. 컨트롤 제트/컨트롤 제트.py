def solution(s):
    result = 0
    for x in range(len(s.split())): # 0~3
        if  s.split()[x] == 'Z':
            result -= int(s.split()[x-1])
        else:
            result += int(s.split()[x])
    return result