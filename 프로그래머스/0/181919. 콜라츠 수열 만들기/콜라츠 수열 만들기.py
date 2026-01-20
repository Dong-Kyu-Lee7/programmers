def solution(n):
    num_lst = [n]

    # while n != 1:
    #     if n % 2 == 0:
    #         n = int(n/2)
    #     else:
    #         n = int(n*3+1)
    #     num_lst.append(n)
    for _ in range(1000):
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 +1
        num_lst.append(n)
    return num_lst
