#!/usr/bin/env python3
with open('/tmp/String.txt') as fojb:
    s = fojb.read() #读取文件内容
res=''
for line in s:
    print(line,end=" ")
    if line.isdigit(): #判断line的值是否为数字，为True时加入到res字符串中
        res+=line
print(" ")
print(res)
