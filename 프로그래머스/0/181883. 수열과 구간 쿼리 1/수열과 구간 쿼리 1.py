def solution(arr, queries):
    for s,e in queries:
        for x in range(s,e+1):
            arr[x] +=1
    return arr