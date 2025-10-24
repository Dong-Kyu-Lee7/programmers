def solution(seoul):
    result = ''
    for x,y in enumerate(seoul):
        if y == "Kim":
            result = f"김서방은 {x}에 있다"
    return result