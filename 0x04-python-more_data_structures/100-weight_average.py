#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    t, s = 0, 0
    for t in my_list:
        t += t[0] * t[1]
        s += t[1]
    return t / s
