def solution(todo_list, finished):
    result = []
    for x in range(len(finished)):
        if finished[x] == False:
            result.append(todo_list[x])
    return result