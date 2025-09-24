def solution(emergency):
    result = []
    for x in emergency:
        result.append(sorted(emergency, reverse = True).index(x)+1)
    return result