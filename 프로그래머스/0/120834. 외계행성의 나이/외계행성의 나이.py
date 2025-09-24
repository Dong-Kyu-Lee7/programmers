import string
def solution(age):
    result = ''
    for x in str(age):
        result += string.ascii_lowercase[int(x)]
    return result