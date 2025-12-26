def solution(slice, n):
    # result = 0
    # if n % slice != 0:
    #     result = (n // slice) +1
    # else:
    #     result = n // slice
    
    if n % slice != 0:
        result = n // slice +1
    else:
        result = n // slice
    return result