def solution(arr, query):
    for x in range(len(query)):
        if x % 2 == 0:
            arr = arr[:query[x]+1]
        else:
            arr = arr[query[x]:]
    return arr