#!/usr/bin/env python3
with open('/etc/passwd') as fobj:
    for line in fobj:
        print(line,end=" ")
