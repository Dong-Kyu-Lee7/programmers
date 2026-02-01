def solution(myString, pat):
    result = 0
    if pat.lower() in myString.lower():
        result = 1
    # else:
    #     result = 0
    return result