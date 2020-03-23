#!/usr/bin/env python3
a = 0
while a<100:
    a=a + 1
    if a%7==0:
        print("\n")
    if a%7 ==0 or  a%10 ==7 or a//10 ==7:
        continue
    else:
        print(a,end=' ')
