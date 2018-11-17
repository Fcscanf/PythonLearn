import sys

print("c:\northwind\northwest")
# 使用转义字符防止换行
print('c:\\northwind\\northwest')
# r''表示输出原始的字符串
print(r'c:\northwind\northwest')
print("hello"[1])

# 条件控制、循环控制、分支
mood = True
if mood:
    print('go to school')
else:
    print('go home')

'''
user login
'''

ACCOUNT = 'fc'
PASSWORD = '123'

# constant 常量大写

print('please input accout')
user_account = input()
print('please input password')
user_password = input()

if ACCOUNT == user_account and PASSWORD == user_password:
    print('success')
else:
    print('fail')

'''
pass 空语句、占位语句
'''
if True:
    pass

'''
循环-递归
'''
COUNTER = 1
while COUNTER <= 10:
    COUNTER +=1
    print(COUNTER)
else:
    print('EOF')

'''
for-主要用来遍历循环序列、集合、字典
'''
a = [['apple','orange','banana','grape'],(1,2,3)]
for x in a:
    for y in x:
        if y == 2:
            # break
            continue
        print(y)
    print('EOF')
else:
    print('fruit is gone')

for x in range(0,10,2):
    print(x,end='|')

A = [1,2,3,4,5,6,7,8]
for i in range(0,len(A),2):
    print(A[i],end=' | ')

B = A[0:len(A):2]
print(B)

print(sys.path)