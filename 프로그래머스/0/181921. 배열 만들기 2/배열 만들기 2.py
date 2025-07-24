def solution(l, r):
    tmp_list = []
    result = []
    for i in range(l,r+1):
        if i % 5 == 0:
            # tmp_list.append(i) # 5 배수값 list

            tmp_str = str(i)
            tmp_list_valid = True    
            for num in tmp_str:
                if num not in ['0', '5']:
                    tmp_list_valid = False
                    break
        
            if tmp_list_valid: # 값이 있다면
                result.append(i)

    if not result:
        return [-1]
    return result