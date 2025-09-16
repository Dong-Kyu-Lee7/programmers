def solution(arr, k):
    result = []
    if k % 2 == 0: # 짝수인 경우
        for x in arr:
            result.append(x+k)
    else: # 홀수인 경우
        for x in arr:
            result.append(x*k)
    return result