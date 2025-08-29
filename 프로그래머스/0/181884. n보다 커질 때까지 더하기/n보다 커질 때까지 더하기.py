def solution(numbers, n):
    result = 0
    
    for x in numbers:
        result += x
        if result > n:
            return result
        
    return result