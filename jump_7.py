#!/usr/bin/env python3
<<<<<<< HEAD
a = 0
while a<100:
    a=a + 1
    if a%7==0:
        print("\n")
    if a%7 ==0 or  a%10 ==7 or a//10 ==7:
        continue
    else:
        print(a,end=' ')
=======
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
>>>>>>> bfb6a805145e537a5fc397adaf424b803ad3defe
