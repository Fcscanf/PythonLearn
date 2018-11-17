list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5]


def square(x):
    return x * x


'''
lambda表达式代替函数
'''
r = map(lambda x: x*x, list_x)
print(list(r))
rp = map(lambda x, y: x*x + y, list_x, list_y)
print(list(rp))
rm = map(square, list_x)
print(list(rm))


