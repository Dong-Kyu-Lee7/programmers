def solution(hp):
    a_num = hp // 5
    b_num = (hp % 5) // 3
    c_num = ((hp % 5) % 3) // 1

    result = a_num+b_num+c_num
    return result