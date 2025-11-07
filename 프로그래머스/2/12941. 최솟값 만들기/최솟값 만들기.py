def solution(A,B):
    A.sort(reverse= True)
    B.sort()

    result = 0
    for l in range(len(A)):
        result += A[l] * B[l]

    return result