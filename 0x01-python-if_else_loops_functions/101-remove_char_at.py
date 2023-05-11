#!/usr/bin/python3
def remove_char_at(str, n):
    sr = ""
    for i in range(len(str)):
        if i != n:
            sr = sr + str[i]
    return (sr)
