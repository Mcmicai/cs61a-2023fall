"""
rational(n, d) 返回分子为 n、分母为 d 的有理数
numer(x) 返回有理数 x 的分子
denom(x) 返回有理数 x 的分母
"""

#我们在这里使用了一个强大的程序设计策略：一厢情愿（wishful thinking）。
#即使我们还没有想好有理数是如何表示的，或者函数 numer、denom 和 rational 应该如何实现。
#但是如果我们确实定义了这三个函数，我们就可以进行加法、乘法、打印和测试有理数是否相等：
def add_rationals(x,y):
    nx, ny = numer(x), denom(x)
    ny, dx = numer(y), denom(y)
    return rational(nx*dy+ny*dx,dx*dy)

def mul_rationals(x,y):
    return rational(numer(x) * numer(y),denom(x) * denom(y))

def print_add_rational(x):
    print(numer(x),'/',denom(x))

def rationals_are_equal(x,y):
    return numer(x) * denom(y) == numer(y) * denom(x)