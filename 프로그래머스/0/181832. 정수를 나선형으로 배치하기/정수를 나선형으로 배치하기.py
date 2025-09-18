def solution(n):
    result = [[0] * n for _ in range(n)]

    mode = 1   # 1: →, 2: ↓, 3: ←, 0: ↑
    row, col = 0, 0

    for val in range(1, n*n + 1):
        result[row][col] = val

        if mode % 4 == 1:        # →
            # 다음 칸 미리 보기
            if col + 1 == n or result[row][col + 1] != 0:
                mode += 1        # 회전
                row += 1         # ↓ 로 한 칸 이동
            else:
                col += 1         # 계속 →
        elif mode % 4 == 2:      # ↓
            if row + 1 == n or result[row + 1][col] != 0:
                mode += 1
                col -= 1         # ← 로 한 칸 이동
            else:
                row += 1
        elif mode % 4 == 3:      # ←
            if col - 1 < 0 or result[row][col - 1] != 0:
                mode += 1
                row -= 1         # ↑ 로 한 칸 이동
            else:
                col -= 1
        else:                    # ↑ (mode % 4 == 0)
            if row - 1 < 0 or result[row - 1][col] != 0:
                mode += 1
                col += 1         # → 로 한 칸 이동
            else:
                row -= 1

    return result