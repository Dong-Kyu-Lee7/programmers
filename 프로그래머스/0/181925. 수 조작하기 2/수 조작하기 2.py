def solution(numLog):
    result = ''
    
    
    for i in range(1,len(numLog)): # 0부터 실행시 'numLog[i-1]' 계산 불가
        if numLog[i] - numLog[i-1] == 1:
            result += 'w'
        elif numLog[i] - numLog[i-1] == -1:
            result += 's'
        elif numLog[i] - numLog[i-1] == 10:
            result += 'd'
        elif numLog[i] - numLog[i-1] == -10:
            result += 'a'
        # else:
        #     result += 'a'
    return result