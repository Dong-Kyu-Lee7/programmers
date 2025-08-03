def solution(number):
    result = 0
    sum = 0
    
    for x in number:
        sum += int(x)
    result = sum % 9
    return result