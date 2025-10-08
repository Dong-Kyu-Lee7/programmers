def solution(dots):
    [[x1,y1], [x2,y2], [x3,y3],[x4,y4]] = dots

    # 1,2 조합 / 3,4 조합
    result1 = ((x1 - x2) * (y3 - y4) ) == ((x3 - x4) * (y1 - y2))

    # 1,3 조합 / 2,4조합
    result2 = ((x1 - x3) * (y2 - y4)) == ((x2 - x4) * (y1 - y3))

    # 1,4 조합 / 2,3 조합
    result3 = ((x1 - x4) * (y2 - y3)) == ((x2 - x3) * (y1 - y4))

    if result1 or result2 or result3:
        result =1
    else:
        result = 0
    return result