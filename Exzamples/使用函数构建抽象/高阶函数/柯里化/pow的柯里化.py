"""
使用高阶函数将一个接受多个参数的函数转换为一个函数链，
每个函数接受一个参数。更具体地说，给定一个函数 f(x, y),
我们可以定义另一个函数 g 使得 g(x)(y) 等价于 f(x, y)。在这里，
g 是一个高阶函数，它接受单个参数 x 并返回另一个接受单个参数 y 的函数。这种转换称为柯里化(Curring)
"""

def curried_pow(x):
    def h(y):
        return pow(x,y)
    return h

print(curried_pow(2)(3))

"""
在 Python 等更通用的语言中,
当我们需要一个只接受单个参数的函数时,柯里化就很有用。
例如,map 模式(map pattern)就可以将单参数函数应用于一串值。
"""

def map_to_range(start, end, f):
    while start<end:
        print(f(start))
        start+=1

#我们可以使用 map_to_range 和 curried_pow 来计算 2 的前十次方，而不是专门编写一个函数来这样做：
print(map_to_range(0,10,curried_pow(2)))

"""
我们手动对 pow 函数进行了柯里化变换，
得到了 curried_pow。
相反,我们可以定义函数来自动进行柯里化,以及逆柯里化变换(uncurrying transformation):
"""

def curry2(f):
    #返回给定的双参数的柯里化版本
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g

def uncurry2(g):
    #返回给定的柯里化函数的双参数版本
    def f(x,y):
        return g(x)(y)
    return f
