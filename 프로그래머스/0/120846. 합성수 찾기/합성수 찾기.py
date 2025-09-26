def solution(n):
    result = 0
    for x in range(1,n+1): # x: 1~10
        c = 0
        for y in range(1,x+1): #y: 1~10
            if x % y == 0:
                c += 1
                
        if c >= 3:
            result += 1
    return result