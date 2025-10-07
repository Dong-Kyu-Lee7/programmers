def solution(spell, dic):
    result = 2
    for x in dic:
        if sorted(x) == sorted(spell):
            result = 1
    return result