#!/usr/bin/python3
print(('{}'*24).format(*[chr(i) for i in range(97, 123) if chr(
    i)not in ('e', 'q')]), end='')
