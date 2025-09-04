def solution(myString, pat):
    result =''
    cond = myString.rfind(pat)
    result = myString[:cond+len(pat)]
    return result