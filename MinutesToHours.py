#!/usr/bin/env python3
import sys
#转换函数
def Hours(min):
#如果为负数则raise异常
    if min<0:
        raise ValueError("Input number cannot be negative")
    else:
        print("{} H,{} M".format(int(min/60),min%60))
#函数调用及异常处理逻辑
try:
    Hours(int(sys.argv[1]))  #获取传入的参数
except:
    print("Parameter Error")
#操作实例 python3 MinutesToHours.py 80
