def solution(left, right):
    result = 0

    for x in range(left,right+1):
        new_count = 0
        for y in range(1,x+1):
            if x % y == 0: # 약수의 개수
                new_count += 1
        if new_count % 2 == 0: # 짝수 경우
            result += x
        else:
            result -= x
    return result