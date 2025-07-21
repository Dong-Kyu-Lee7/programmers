def solution(arr, queries):
    result = []
    
    for s,e,k in queries:
        temp_list = []
        for x in arr[s:e+1]:
            # print(x)
            if x > k:
                # print(x)
                temp_list.append(x)
                # print(temp_list)
        if temp_list:
            result.append(min(temp_list))
            # print(result)
        else:
            result.append(-1)
    return result