def solution(code):
    answer = ''
    mode = 0
    
    for idx, code in enumerate(code):
        if code == '1':
            if mode == 1:
                mode = 0
            else: # mode != 1
                mode = 1
        
        else:
            if mode == 0:
                if idx % 2 == 0 and code != '1':
                    answer += code
            else:
                if idx % 2 == 1 and code != '1':
                    answer += code
    
    if answer == '':
        answer = 'EMPTY'
    
    return answer
    