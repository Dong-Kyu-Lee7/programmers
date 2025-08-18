def solution(arr, idx):
    
    for x in range(idx, len(arr)):
        if arr[x] == 1:
            return  x
        
    return -1