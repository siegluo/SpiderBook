# -*- coding: utf-8 -*-
def generater():
    n = 1
    while True:
        yield n
        n += 1


def createCounter():
    g = generater()

    def counter():
        return next(g)

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
