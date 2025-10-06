def solution(numbers):
    result = []
    for x_idx,x_val in enumerate(numbers):
        for y_idx,y_val in enumerate(numbers):
            if x_idx == y_idx:
                continue
            result.append(x_val * y_val)
    return max(result)