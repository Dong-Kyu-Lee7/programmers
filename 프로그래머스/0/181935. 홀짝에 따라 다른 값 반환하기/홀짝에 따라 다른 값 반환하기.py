def solution(n):
#     answer = 0
    
#     if n % 2 == 1:
#         for i in range(1, n+1):
#             if i % 2 == 1:
#                 answer += i
#     else:
#         for i in range(1, n+1):
#             if i % 2 == 0:
#                 answer += (i ** 2)
    result = 0

    # even
    if n % 2 == 0:
        for x in range(2, n+1, 2):
            result += (x ** 2)
        # odd
    else:
        result += sum(range(1, n+1, 2))
    return result