def solution(arr, queries):
    result = arr
    for i in range(len(queries)):
        a = queries[i][0]
        b = queries[i][1]
        
        result[a], result[b] = result[b], result[a]
    return result