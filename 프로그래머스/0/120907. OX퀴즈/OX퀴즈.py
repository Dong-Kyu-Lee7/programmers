def solution(quiz):
    result = []
# ' '.join(eval(str(quiz[x].split()[:3])))
    for x in quiz:
        part = x.split()
        problem = ' '.join(part[:3])
        answer = int(part[4])
        if eval(problem) == answer:
            result.append('O')
        else:
            result.append('X')
    return result