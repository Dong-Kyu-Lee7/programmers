def solution(arr1, arr2):
    result = []
    for x in range(len(arr1)):
        tmp = []
        for y in range(len(arr1[0])):
            tmp.append(arr1[x][y] + arr2[x][y])
        result.append(tmp)
    return result