def solution(hp):
    g,s,w = 5,3,1
    g_num = hp // g
    s_num = (hp % g) // s
    w_num = ((hp % g) % s) // w

    result = g_num + s_num + w_num
    return result