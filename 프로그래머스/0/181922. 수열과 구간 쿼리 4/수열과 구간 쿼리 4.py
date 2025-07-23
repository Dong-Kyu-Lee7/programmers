def solution(arr, queries):
    answer = []
    
    for s,e,k in queries:
        for x in range(s,e+1):
            if x % k == 0:
                arr[x] += 1
    
    return arr