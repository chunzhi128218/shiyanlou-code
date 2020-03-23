#!/usr/bin/env python3
a = 1
while a < 101:
    if a%7 == 0:
        pass
    elif a//10 == 7:
        pass
    elif a%10 == 7:
        a = a + 1
        continue
    else:
        print(a, end=" ")
    a = a + 1
