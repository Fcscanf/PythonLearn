def add(x, y):
    return x + y


print(add(1, 2))
# 关键字参数
print(add(y=3, x=2))


def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1, damage2


skill1_damage, skill2_damage = damage(3, 6)
print(skill1_damage, skill2_damage)
damages = damage(3, 6)
print(damages[0], damages[1])
print(type(damages))

'''
序列解包
'''
a, b, c = 1, 2, 3
d = 4, 5, 6
e, f, g = d
