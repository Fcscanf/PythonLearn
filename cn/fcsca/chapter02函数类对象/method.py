# 匿名函数 lambda
def add(x, y):
    return x + y


print(add(1, 2))

f = lambda x, y: x + y
print(f(1, 2))

'''
三元表达式
条件为真的结果 if 条件判断 else 条件为假返回的结果
'''
x = 2
y = 1
r = x if x > y else y
print(r)
