import re
'''
* 匹配前面的元素一次或者多次
+ 匹配一次或者多次
？匹配0次或者1次
4,8 边界匹配，最大位数最小位数
'''
a = 'python0python1pythonn2'
r = re.findall('',a)
print(r)