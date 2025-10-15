def solution(A, B):
    result = -1
    if A == B:
        result = 0
    for x in range(1,len(A)): # 1,5
        A = A[-1] + A[:-1]
        if A == B:
            result = x
            break
    return result