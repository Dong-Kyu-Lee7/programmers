def solution(keyinput, board):
    result = [0,0]
    for x in keyinput:
        if x == 'left':
            result[0] -= 1
            if abs(result[0]) > board[0] // 2:
                result[0] += 1
        elif x == 'right':
            result[0] += 1
            if abs(result[0]) > board[0] // 2:
                result[0] -= 1
        elif x == 'up':
            result[1] += 1
            if abs(result[1]) > board[1] // 2:
                result[1] -= 1
        elif x == 'down':
            result[1] -= 1
            if abs(result[1]) > board[1] // 2:
                result[1] += 1
    return result