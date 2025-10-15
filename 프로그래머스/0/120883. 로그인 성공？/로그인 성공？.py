def solution(id_pw, db):
    result = 'fail'
    for x in db:
        if x == id_pw:
            result = 'login'
        elif x[0] == id_pw[0]:
            result = 'wrong pw'
    return result