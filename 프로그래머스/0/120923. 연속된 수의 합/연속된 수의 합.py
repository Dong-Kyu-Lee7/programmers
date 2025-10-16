def solution(num, total):
    result = []
    avg = total // num # 4
    for x in range(avg - ((num-1) // 2), avg + ((num+2) // 2)):
        result.append(x)
    return result