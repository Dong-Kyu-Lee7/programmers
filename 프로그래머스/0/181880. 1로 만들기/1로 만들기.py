def solution(num_list):
    result = 0

    for x in num_list:
        count = 0 # 연산 횟수

        while x != 1:
            count += 1 # 연산 횟수 카운팅
            if x % 2 == 0:
                x //= 2
            else:
                x = (x-1) // 2

        result += count
    return result