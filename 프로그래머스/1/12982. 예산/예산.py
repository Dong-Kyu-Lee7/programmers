def solution(d, budget):
    answer = 0
    total = 0
    d = sorted(d)

    for x in range(len(d)):
        if total + d[x] <= budget:
            total += d[x]
            answer += 1
    return answer