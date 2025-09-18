def solution(board, k):
    result = 0

    for x in range(len(board)):
        for y in range(len(board[x])):
            if (x + y) <= k:
                result += board[x][y]
    return result