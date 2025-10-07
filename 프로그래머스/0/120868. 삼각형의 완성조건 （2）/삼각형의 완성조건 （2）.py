def solution(sides):
    # 1) sides 중 가장 긴변인 경우(이등변삼각형) -> sides 중 가장 긴변 이하 & 가장 작은 변 초과 포함
    # 2) 아예 나머지 변이 가장 긴변인 경우 -> sides 합 미만 & sides 중 가장 긴 변 초과
    result = 0

    max_counts = 0
    for x in range(max(sides) - min(sides)+1, max(sides)+1):
        print(x)
        max_counts += 1

    another_counts = 0
    for y in range(max(sides)+1, sum(sides)):
        print(y)
        another_counts += 1

    result = max_counts + another_counts
    return result