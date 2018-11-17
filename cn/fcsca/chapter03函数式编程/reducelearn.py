from functools import reduce

'''
连续计算，连续调用,第三个参数可以作为初始参数
（（（1+2）+3）+4）
'''

list_x = [1, 2, 3, 4, 5, 6, 7, 8]
r = reduce(lambda x, y: x + y, list_x, 10)
print(r)

list_y = ['1', '2', '3', '4', '5', '6', '7', '8']
rq = reduce(lambda x, y: x + y, list_y, 'abc')
print(rq)
