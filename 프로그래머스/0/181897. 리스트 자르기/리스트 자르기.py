def solution(n, slicer, num_list):
    if n == 1:
        result = num_list[:slicer[1]+1]
    elif n == 2:
        result = num_list[slicer[0]:]
    elif n == 3:
        result = num_list[slicer[0]:slicer[1]+1]
    elif n == 4:
        result = num_list[slicer[0]:slicer[1]+1:slicer[2]]
    return result