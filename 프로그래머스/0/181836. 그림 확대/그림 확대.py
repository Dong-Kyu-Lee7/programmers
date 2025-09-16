def solution(picture, k):
    result = []
    
    for x in picture:
        resized = ''
        for pixel in x:
            resized += pixel * k

        for _ in range(k):
            result.append(resized)
    return result