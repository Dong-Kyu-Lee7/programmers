def solution(board):
    result = 0
    n = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1] # 좌우상하대각선 순
    dy = [0, 0, -1, 1, -1, 1, -1, 1] # 좌우상하대각선 순
    boom = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1: # 지뢰 위치
                boom.append((i, j))
    for x, y in boom:
        for i in range(8):
            nx = x + dx[i] # 지뢰 위치 기준 좌우상하대각선 위험지역 예비
            ny = y + dy[i] # 지뢰 위치 기준 좌우상하대각선 위험지역 예비
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 1 # 위험지역 확정
    for i in board:
        result += i.count(0) # 안정지역 개수
    return result